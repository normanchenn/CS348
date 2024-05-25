from flask import Blueprint, jsonify

api_v1 = Blueprint("api", __name__, url_prefix="/api/v1")


@api_v1.route("/")
def home():
    return jsonify({"hello": "world"})
