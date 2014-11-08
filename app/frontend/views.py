from flask import Blueprint

frontend = Blueprint('frontend', __name__, template_folder='templates', static_folder='static')



@frontend.route('/')
def index():
	return "hello from frontend"
