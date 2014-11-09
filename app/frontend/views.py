import json
import os
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.stormpath import StormpathError, login_required, User, login_user, logout_user, user

from app.api.models import users_collection


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
JSON_URL = os.path.join(SITE_ROOT, "json_data/")


frontend = Blueprint(
    'frontend', __name__, template_folder='templates', static_folder='static')


@frontend.route('/')
@frontend.route('/index')
@login_required
def index():
    userId = user.get_id()
    _user = users_collection.find({"_id": userId})
    users = users_collection.find().count()
    print "Numero de usuarios es {}".format(users)

    # verificamos que el usuario existe
    if _user.count() is 0:
        data = {
            "_id": userId,
            "user_id": users + 1,
            "email": user.email,
            "name": user.given_name,
            "surname": user.surname,
            "username": user.username,
            "fullname": user.given_name + ' ' + user.surname
        }

        users_collection.insert(data)
        return redirect(url_for('.index'))
    # si no existe
    else:
        return render_template(
            'index.html',
            _id=userId,
            mail=user.email,
            name=user.full_name,
            
        )


@frontend.route('/create')
@login_required
def create():
    return render_template('create.html')


@frontend.route('/preview')
@login_required
def preview():
    return render_template('preview.html')
