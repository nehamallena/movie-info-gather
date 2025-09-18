from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"   # 👉 Replace with OMDb API key
BASE_URL = "http://www.omdbapi.com/"

@app.route("/", methods=["GET", "POST"])
def home():
    movie = None
    related_movies = None
    default_movies = []

    if request.method == "POST":
        movie_name = request.form["movie"]
        response = requests.get(BASE_URL, params={"t": movie_name, "apikey": API_KEY})
        movie = response.json()

        # related movies
        if "Title" in movie:
            search_resp = requests.get(BASE_URL, params={"s": movie["Title"].split()[0], "apikey": API_KEY})
            data = search_resp.json()
            related_movies = data.get("Search", [])
    else:
        # default movies (carousel/grid)
        default_titles = ["Inception", "Avatar", "Titanic", "Avengers", "The Dark Knight"]
        for t in default_titles:
            resp = requests.get(BASE_URL, params={"t": t, "apikey": API_KEY})
            default_movies.append(resp.json())

    return render_template("index.html", movie=movie, related_movies=related_movies, default_movies=default_movies)

if __name__ == "__main__":
    app.run(debug=True)
