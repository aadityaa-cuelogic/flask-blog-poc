from flask import Flask

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	SECRET_KEY="MY_SECRET_KEY",
	from_object=__name__,
	SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db'
)
from blog import views, models

app.register_blueprint(views.blueprint_blog)