"""
Routes for api
"""

# imports
from flask import Blueprint, jsonify
from ..services.api_service import get_test_value

api_v1 = Blueprint("api", __name__, url_prefix="/api/v1")


@api_v1.route("/")
def home():
    """Entry point of app (root directory)

    Returns:
        str: hello world
    """
    return jsonify({"hello": "world"})


@api_v1.route("/test/<key>")
def test(key):
    """Test the values from api endpoint

    Args:
        key (str): API key for the endpoint

    Returns:
        data (json): Return data retrieved
    """
    print(key)
    return jsonify(get_test_value(key))
