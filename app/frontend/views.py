import json
import os
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.stormpath import StormpathError, login_required, User, login_user, logout_user, user
from app.api.models import users_collection, gamedata_collection, rules_collection



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
@frontend.route('/skills')
def skills():
	rules = rules_collection.find_one()
	rules_page = len(rules["skills"]) / 3

	return render_template(
		'skills.html',
		rules=rules,
		rules_page=rules_page

	)


@frontend.route('/personal')
def personal():
	return render_template('personal.html')

@frontend.route('/swag')
def swag():
	return render_template('swag.html')


@frontend.route('/create')
def create():
	rules = rules_collection.find_one()
	
	return render_template(
		'create.html',
		rules=rules
	)


@frontend.route('/character')
def preview():
    return render_template('character.html')
