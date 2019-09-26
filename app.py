from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # OUR MOCK ARRAY OF PROJECTS
    '''
    playlists = [
        {'title': 'Cat Videos', 'description': 'Cats acting weird'},
        {'title': '80\'s Music', 'description': 'Don\'t stop believing!'},
        {'title': 'Spirituality', 'description': 'Majalis-e-Aza'}
        ]
    '''
    return render_template('playlists_index.html', playlists=playlists.find())


@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)


@app.route('/playlists/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('playlists_new.html', playlist={},
                           title='New Playlist')


'''
def playlists_cancel():
    """Redirect to the homepage if user cancels."""
    return redirect(url_for('playlists_show.html', cancel='cancel'))
'''


@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
        # 'rating': request.form.get('rating')
    }
    playlist_id = playlists.insert_one(playlist).insert_id
    return redirect(url_for('playlists_show', playlist_id=playlist_id))


@app.route('/playlists/<playlist_id>')
def playlists_show(playlist_id):
    """Show a single playlist."""
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_show.html', playlist=playlist)


@app.route('/playlists/<playlist_id>/edit')
def playlists_edit(playlist_id):
    """Show the edit form for a playlist."""
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    # video_links = '\n'.join(playlist.get('videos'))
    return render_template('playlists_edit.html', playlist=playlist,
                           title='Edit Playlist')


@app.route('/playlists/<playlist_id>', methods=['POST'])
def playlists_update(playlist_id):
    """Submit an edited playlist."""
    updated_playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.update_one(
        {'_id': ObjectId(playlist_id)},
        {'$set': updated_playlist})
    return redirect(url_for('playlists_show', playlist_id=playlist_id))


@app.route('/playlists/<playlist_id>/delete', methods=['POST'])
def playlist_delete(playlist_id):
    """Delete one playlist."""
    playlist.delete_one({'_id': ObjectId(playlist_id)})
    return redirect(url_for('playlists_index'))


# @app.route('play')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
