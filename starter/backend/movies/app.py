from flask import Flask
from movies.movies_api import movies_bp

app = Flask(__name__)
app.register_blueprint(movies_bp)

@app.route("/")
def health():
    return {"status": "ok"}
