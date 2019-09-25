from flask import Flask, render_template
from pymongo import MongoClient


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
