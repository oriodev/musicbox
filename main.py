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
        all_related_artists.append({'name': a['name'], 'link': a['external_urls']['spotify']})
    
    return all_related_artists

def get_all_related_artists(artists):
    all_related_artists = []

    for i in range(len(artists)):
        artist = get_artist_id(artists[i])
        all_related_artists.extend(get_related_artists(artist))
    
    return random.sample(all_related_artists, 5)
