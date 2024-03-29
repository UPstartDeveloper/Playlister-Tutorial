from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId

from app.util import get_db

db = get_db()

playlists = Blueprint("playlists", __name__)


@playlists.route("/")
def playlists_index():
    """Show all playlists."""
    return render_template("playlists_index.html", playlists=db.playlists.find())


@playlists.route("/playlists/new")
def playlists_new():
    """Create a new playlist."""
    return render_template("playlists_new.html", playlist={}, title="New Playlist")


@playlists.route("/playlists", methods=["POST"])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        "title": request.form.get("title"),
        "description": request.form.get("description"),
        "videos": request.form.get("videos").split(),
    }
    print(playlist)
    playlist_id = db.playlists.insert_one(playlist).inserted_id
    return redirect(url_for("playlists.playlists_show", playlist_id=playlist_id))


@playlists.route("/playlists/<playlist_id>", methods=["GET"])
def playlists_show(playlist_id):
    """Show a single playlist."""
    playlist = db.playlists.find_one({"_id": ObjectId(playlist_id)})
    playlists_comments = db.comments.find({"playlist_id": ObjectId(playlist_id)})
    return render_template(
        "playlists_show.html", playlist=playlist, comments=playlists_comments
    )


@playlists.route("/playlists/<playlist_id>/edit")
def playlists_edit(playlist_id):
    """Show the edit form for a playlist."""
    playlist = db.playlists.find_one({"_id": ObjectId(playlist_id)})
    # video_links = '\n'.join(playlist.get('videos'))
    return render_template(
        "playlists_edit.html", playlist=playlist, title="Edit Playlist"
    )


@playlists.route("/playlists/<playlist_id>", methods=["POST"])
def playlists_update(playlist_id):
    """Submit an edited playlist."""
    updated_playlist = {
        "title": request.form.get("title"),
        "description": request.form.get("description"),
        "videos": request.form.get("videos").split(),
    }
    db.playlists.update_one({"_id": ObjectId(playlist_id)}, {"$set": updated_playlist})
    return redirect(url_for("playlists.playlists_show", playlist_id=playlist_id))


@playlists.route("/playlists/<playlist_id>/delete", methods=["POST"])
def playlist_delete(playlist_id):
    """Delete one playlist."""
    db.playlists.delete_one({"_id": ObjectId(playlist_id)})
    return redirect(url_for("playlists.playlists_index"))
