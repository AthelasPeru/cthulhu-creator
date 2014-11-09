from flask import Blueprint, render_template
from flask.ext.stormpath import StormpathError, login_required, User, login_user, logout_user, user


frontend = Blueprint(
    'frontend', __name__, template_folder='templates', static_folder='static')


@frontend.route('/')
@frontend.route('/index')
@login_required
def index():
    return render_template('index.html')


@frontend.route('/create')
@login_required
def create():
    return render_template('create.html')


@frontend.route('/preview')
@login_required
def preview():
    return render_template('preview.html')
