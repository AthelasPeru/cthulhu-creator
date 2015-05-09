import json
import os
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.stormpath import StormpathError, login_required, User, login_user, logout_user, user
from app.api.models import users_collection



SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
JSON_URL = os.path.join(SITE_ROOT, "json_data/")


frontend = Blueprint(
    'frontend', __name__, template_folder='templates', static_folder='static_front')


@frontend.route('/')
@frontend.route('/index')
def index():
    
    return render_template(
        'index.html'
        
    )


@frontend.route('/create')
@login_required
def create():
    return render_template('create.html')


@frontend.route('/preview')
@login_required
def preview():
    return render_template('preview.html')
