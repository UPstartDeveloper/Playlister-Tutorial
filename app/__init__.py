from flask import Flask
from app.comments.routes import comments_bp
from app.playlists.routes import playlists_bp


def create_app():
    """Init the app, and all the same routes as we had before."""
    app = Flask(__name__)
    app.register_blueprint(playlists_bp)
    app.register_blueprint(comments_bp)
    return app
