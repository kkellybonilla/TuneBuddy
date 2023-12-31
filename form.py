from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Optional, Length

class SongForm(FlaskForm):
    lyrics = StringField("Tell me the lyrics you remember, even if it's just a few, and I'll try my best to find your song! ", validators=[DataRequired(), Length(min=3, max=150, message='Invalid lyric length. Must be between 3-50 characters.')], render_kw={"autocomplete": "off", "placeholder": "Do re mi fa so la ti do... "})
    artist_name = StringField('Artist Name: ', validators=[Optional(), Length(min=3, max=50, message='Invalid artist name. Must be between 3-50 characters.')], render_kw={"autocomplete": "off", "placeholder": "Optional"})
    genre = StringField('Genre: ', validators=[Optional(), Length(min=3, max=50, message='Invalid genre. Must be between 3-50 characters.')], render_kw={"autocomplete": "off", "placeholder": "Optional"})
    submit = SubmitField('Find My Tune!')
