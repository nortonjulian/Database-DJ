"""Forms for playlist app."""

from wtforms import SelectField, StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("name", validators=[InputRequired()])


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("title", validators=[InputRequired()])
    artist = StringField("artist", validators=[InputRequired()])
    length = IntegerField("length", validators=[InputRequired()])
    submit = SubmitField("Add Song")

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
