from flask import Flask
from app.playlists.routes import playlists_bp


def create_app():
    """Init the app, and all the same routes as we had before."""
    app = Flask(__name__)
    app.register_blueprint(playlists_bp)
    return app
