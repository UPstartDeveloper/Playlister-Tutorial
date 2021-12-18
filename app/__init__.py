from flask import Flask
from app.comments.routes import comments
from app.playlists.routes import playlists


def create_app():
    """Init the app, and all the same routes as we had before."""
    app = Flask(__name__)
    app.register_blueprint(playlists)
    app.register_blueprint(comments)
    return app
