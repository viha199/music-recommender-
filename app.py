from flask import Flask, render_template, request
from recommender import get_songs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    songs = []

    if request.method == "POST":
        mood = request.form.get("mood")
        language = request.form.get("language")

        if mood and language:
            songs = get_songs(mood, language)

    return render_template("index.html", songs=songs)

if __name__ == "__main__":
    app.run(debug=True)