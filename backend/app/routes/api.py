from flask import Blueprint, jsonify
from ..services.api_service import get_test_value

api_v1 = Blueprint("api", __name__, url_prefix="/api/v1")


@api_v1.route("/")
def home():
    return jsonify({"hello": "world"})


@api_v1.route("/test/<key>")
def test(key):
    print(key)
    return jsonify(get_test_value(key))
