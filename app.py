from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template('index.html')
    
    if request.method == "POST":
        return redirect("/results")

@app.route("/results", methods=["GET", "POST"])
def results():

    if request.method == "GET":
        return render_template('results.html')
    if request.method == "POST":
        return redirect("/")