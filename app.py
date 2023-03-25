from flask import Flask, render_template, request, redirect, session
from main import get_all_related_artists, get_artist_id

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
    
        # IF ANY BOXES ARE LEFT EMPTY THEN IT FAILS

        if not artist1 or not artist2 or not artist3:
            return redirect("/")

       # PUT ARTISTS INTO LIST

        artists = []
        artists.extend([artist1, artist2, artist3])

        # CHECK ALL ARTISTS ARE IN SPOTIFY DATABASE

        for i in range(len(artists)):
            if get_artist_id(artists[i]) == False:
                return redirect("/")

        # GET 5 ARTIST RECOMMENDATIONS FROM LIST OF ARTISTS

        artist_recs = get_all_related_artists(artists)
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