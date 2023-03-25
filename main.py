import spotipy, sys, random, os

from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# GET ACCESS TOKEN

load_dotenv()

if not os.getenv("client_id"):
    raise RuntimeError("API_KEY not set")

if not os.getenv("client_secret"):
    raise RuntimeError("API_KEY not set")

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

# GET ARTIST

def get_artist_id(name):
    artist = sp.search(q='artist:' + name, type='artist', limit=1)

    if len(artist['artists']['items']) != 0:
        return artist['artists']['items'][0]['uri']
    else:
        return False

def get_related_artists(artist):
    related_artists = sp.artist_related_artists(artist)['artists']
    all_related_artists = []

    for a in related_artists[:10]:
        all_related_artists.append({'name': a['name'], 'link': a['external_urls']['spotify'], 'image': a['images'][0]['url']})
    
    return all_related_artists

def get_all_related_artists(inputted_artists, num_of_recs):
    all_related_artists = []

    for i in range(len(inputted_artists)):
        artist = get_artist_id(inputted_artists[i])
        all_related_artists.extend(get_related_artists(artist))
    
    return select_random_artists(all_related_artists, inputted_artists, num_of_recs)

def is_artist_in_list(artist, list):

    for i in range(len(list)):
        try:
            if get_artist_id(artist) == get_artist_id(list[i]['name']):
                return True
        except:
            if get_artist_id(artist) == get_artist_id(list[i]):
                return True
        
    return False

def select_random_artists(all_related_artists, inputted_artists, num_of_recs):

    artist_list = []
    
    while (len(artist_list) < int(num_of_recs)):
        artist = random.sample(all_related_artists, 1)

        if is_artist_in_list(artist[0]['name'], artist_list) == False: 
            if artist not in inputted_artists: 
                artist_list.append(artist[0])
    
    return artist_list
