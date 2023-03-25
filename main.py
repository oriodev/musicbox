import spotipy, sys, random, os

from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


# GET ACCESS TOKEN

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

def main():
    artist_recs = []

    for i in range(3):
        get_artist(artist_recs)
    
    for artist in return_random_artists(artist_recs):
        print(artist)


# GET ARTIST

def get_artist(artist_recs):

    while len(artist_recs) < 30:

        name = input("artist name: ")

        results = sp.search(q='artist:' + name, type='artist', limit=1)

        if len(results['artists']['items']) != 0:

            artist_id = results['artists']['items'][0]['uri']

            related_artists = sp.artist_related_artists(artist_id)
            related_artists = related_artists['artists']
            for a in related_artists[:10]:
                temp_dic = {}
                temp_dic['name'] = a['name']
                temp_dic['link'] = a['external_urls']['spotify']
                artist_recs.append(temp_dic)

def return_random_artists(artist_recs):
    return random.sample(artist_recs, 5)

main()