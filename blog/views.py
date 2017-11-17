from flask import Blueprint, request, url_for, render_template
from . models import User, Post, db
from . forms import AddPost
blueprint_blog = Blueprint('blog', __name__, url_prefix="/")



@blueprint_blog.route("/")
def index():
	posts = Post.query.all()
	return render_template("post.html", posts=posts)

@blueprint_blog.route("addpost", methods=['GET','POST'])
def addpost():
	if request.method == 'GET':
		postform = AddPost()
		return render_template("addpost.html", postform=postform)
	else:
		return "POST method"


