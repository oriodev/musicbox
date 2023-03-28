import spotipy, sys, random, os

from spotipy import util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# GET ACCESS TOKEN

load_dotenv()

if not os.getenv("client_id"):
    raise RuntimeError("API_KEY not set")

if not os.getenv("client_secret"):
    raise RuntimeError("API_KEY not set")

if not os.getenv("redirect_uri"):
    raise RuntimeError("REDIRECT_URI not set")

if not os.getenv("username"):
    raise RuntimeError("USERNAME not set")

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")
username = os.getenv("username")
scope="playlist-modify-public"
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
	client_id = client_id,
	client_secret = client_secret,
	redirect_uri = redirect_uri,
	scope=scope
))

# GET USER ID

sp = spotipy.client.Spotify(auth=token)
user_id = sp.me()['id']

#
#
# GENERATING A PLAYLIST
#
#

def make_playlist():
    playlist = sp.user_playlist_create(user_id, 'name', public=True, collaborative=False, description='')
    return playlist["id"]


def add_songs_to_playlist(playlist):
    playlist_add_items(playlist_id, items, position=None)

print(make_playlist())

# 
#
# GENERATING RECOMMENDATIONS
#
#

# GET ARTIST

def get_artist(name):
    artist = sp.search(q='artist:' + name, type='artist', limit=1) # CALLS API

    if len(artist['artists']['items']) != 0:
        return artist
    else:
        return False

def get_artist_id(artist):
    # artist = sp.search(q='artist:' + name, type='artist', limit=1) # CALLS API

    if len(artist['artists']['items']) != 0:
        return artist['artists']['items'][0]['uri']
    else:
        return False

# GET RELATED ARTISTS FROM AN ARTIST

def get_related_artists(artist):
    related_artists = sp.artist_related_artists(artist)['artists'] # CALLS API
    all_related_artists = []

    for a in related_artists[:10]:
        all_related_artists.append({'name': a['name'], 'link': a['external_urls']['spotify'], 'image': a['images'][0]['url']})
    
    return all_related_artists

# GET ALL THE RELATED ARTISTS FROM ALL THE ARTISTS

def get_all_related_artists(inputted_artists, num_of_recs):
    all_related_artists = []

    for i in range(len(inputted_artists)):
        artist = get_artist_id(get_artist(inputted_artists[i]))
        all_related_artists.extend(get_related_artists(artist)) # CALLS API 3 TIMES
    
    return select_random_artists(all_related_artists, inputted_artists, num_of_recs)

# CHECKS IF THE ARTIST IS IN THE INPUTTED LIST

def is_artist_in_list(artist, list):

    list_length = len(list)

    for i in range(list_length):
        if artist[0]['name'] == list[i]['name']:
            return True
        
    return False

# SELECT RANDOM ARTISTS TO RETURN

def select_random_artists(all_related_artists, inputted_artists, num_of_recs):

    artist_list = []
    
    while (len(artist_list) < int(num_of_recs)):
        artist = random.sample(all_related_artists, 1)

        if is_artist_in_list(artist, artist_list) == False: 
            if artist[0]['name'] not in inputted_artists:
                artist_list.append(artist[0])
    
    return artist_list