from flask import Blueprint, render_template

frontend = Blueprint(
    'frontend', __name__, template_folder='templates', static_folder='static')


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/create')
def create():
    return render_template('create.html')


@frontend.route('/preview')
def preview():
    return render_template('preview.html')
