from flask import Blueprint, request, redirect, url_for
from bson.objectid import ObjectId

from app.util import get_db

db = get_db()

comments = Blueprint("comments", __name__)


@comments.route("/playlists/comments", methods=["POST"])
def comments_new():
    """Submit a new comment."""
    comment = {
        "title": request.form.get("title"),
        "content": request.form.get("content"),
        "playlist_id": ObjectId(request.form.get("playlist._id")),
    }
    print(comment)
    comment_id = db.comments.insert_one(comment).inserted_id
    return redirect(
        url_for("playlists.playlists_show", playlist_id=request.form.get("playlist._id"))
    )


@comments.route("/playlists/comments/<comment_id>", methods=["POST"])
def comments_delete(comment_id):
    """Action to delete a comment."""
    if request.form.get("_method") == "DELETE":
        comment = db.comments.find_one({"_id": ObjectId(comment_id)})
        playlist_id = comment.get("playlist_id")
        db.comments.delete_one({"_id": ObjectId(comment_id)})
        return redirect(url_for("playlists.playlists_show", playlist_id=playlist_id))
