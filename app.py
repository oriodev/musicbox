from flask import Flask, render_template, request, redirect
from main import get_all_related_artists

app = Flask(__name__)

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
       
       # GET LIST OF ARTIST RECOMMENDATIONS TO DISPLAY
        artists = []
        artists.extend([artist1, artist2, artist3])

        artist_recs = get_all_related_artists(artists)
        
        return redirect("/results")

@app.route("/results", methods=["GET", "POST"])
def results():

    if request.method == "GET":
        print(artist_recs)
        return render_template('results.html')
    if request.method == "POST":
        return redirect("/")