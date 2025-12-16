from flask import Blueprint, jsonify

movies_bp = Blueprint("movies", __name__)

@movies_bp.route("/movies")
def get_movies():
    return jsonify([
        {"id": 1, "title": "The Matrix"},
        {"id": 2, "title": "Inception"}
    ])
