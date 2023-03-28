from flask import Flask, render_template, request, redirect, session, flash
from main import get_all_related_artists, get_artist_id, get_artist, is_artist_in_list
from main import choose_songs_to_add_to_playlist, add_songs_to_playlist, make_playlist, get_playlist_cover

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# FRONT PAGE

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template('index.html')
    
    if request.method == "POST":

        # DECLARE ARTIST REC LIST

        artist_recs = []

        # GET ARTISTS FROM FORM
    
        artist1 = request.form.get("artist-one")
        artist2 = request.form.get("artist-two")
        artist3 = request.form.get("artist-three")
        num_of_recs = request.form.get("number")
    
        # IF ANY BOXES ARE LEFT EMPTY THEN IT FAILS

        if not artist1 or not artist2 or not artist3:
            flash("input 3 artists")
            return redirect("/")

       # PUT ARTISTS INTO LIST

        inputted_artists = []
        inputted_artists.extend([artist1, artist2, artist3])
        length = len(inputted_artists)

        # CHECK ALL ARTISTS ARE IN SPOTIFY DATABASE, ADD TO LIST IF THEY ARE

        for i in range(length):
            input = get_artist(inputted_artists[i])
            if input != False:
                inputted_artists[i] = input['artists']['items'][0]['name']
            else:
                flash("one or more artists not in database")
                return redirect("/")

        # CHECK IF ALL ARTISTS ARE DISTINCT
            if length > len(set(inputted_artists)):
                flash("artists must be unique")
                return redirect("/")

        # GET ARTIST RECOMMENDATIONS FROM LIST OF ARTISTS

        artist_recs = get_all_related_artists(inputted_artists, num_of_recs)
        session['artist_recs'] = artist_recs
        
        return redirect("/results")

# RESULTS PAGE

@app.route("/results", methods=["GET", "POST"])
def results():

    if request.method == "GET":
        artist_recs = session['artist_recs']
        return render_template('results.html', artist_recs=artist_recs)
    if request.method == "POST":
        return redirect("/")

@app.route("/playlist", methods=["GET", "POST"])
def playlist():

    if request.method == "GET":
        return render_template("playlist.html")
    
    if request.method == "POST":
        artists = request.form.getlist('selected_artists')
        session['songs_to_add'] = []
        session['songs_to_add'] = choose_songs_to_add_to_playlist(artists)

        return render_template("playlist.html", songs=session['songs_to_add'])

@app.route("/confirmation", methods=["GET", "POST"])
def confirmation():

    if request.method == "GET":
        return render_template("confirmation.html")
    
    if request.method == "POST":

        playlist_name = request.form.get('playlist_name')
        songs_to_add = session['songs_to_add']
        playlist_id = make_playlist(playlist_name)
        
        add_songs_to_playlist(playlist_id, songs_to_add)

        playlist_cover = get_playlist_cover(playlist_id)[0]['url']


        return render_template("confirmation.html", playlist_cover=playlist_cover, playlist_name=playlist_name)
