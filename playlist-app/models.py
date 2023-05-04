"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text(100), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)

class Song(db.Model):
    """Song."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text(100), nullable=False, unique=True)
    artist = db.Column(db.Text(100), nullable=False, unique=True)
    length = db.Column(db.Integer, nullable=False, unique=True)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Text, nullable=False)
    song_id = db.Column(db.Text, nullable=False)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
