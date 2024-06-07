"""
Entry point for the flask routes
"""

from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    """Home Route

    Returns:
        hello world (str): hello world string
    """
    return "<p>hello world</p>"
