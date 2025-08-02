from flask import Flask, render_template, request
from scraper import buscar_videos_por_hashtag

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    videos = []
    if request.method == "POST":
        hashtag = request.form.get("hashtag", "").strip().lstrip("#")
        if hashtag:
            videos = buscar_videos_por_hashtag(hashtag)
    return render_template("index.html", videos=videos)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
