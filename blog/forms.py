from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class AddPost(FlaskForm):
	title = TextField('Title', validators=[ DataRequired() ])
	description = TextField('Description', validators= [ DataRequired() ])
	submit = SubmitField('Post')