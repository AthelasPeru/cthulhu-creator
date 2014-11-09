from flask import Flask
from flask.ext.stormpath import StormpathManager
from config import DEBUG
from private.config import (
    CSRF_SECRET_KEY,
    SECRET_KEY,
    STORMPATH_API_KEY_FILE,
    FACEBOOK_APP_ID,
    FACEBOOK_APP_SECRET,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET
)

app = Flask(__name__)
app.config['debug'] = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY


app.config['STORMPATH_API_KEY_FILE'] = STORMPATH_API_KEY_FILE
app.config['STORMPATH_REDIRECT_URL'] = '/'
app.config['STORMPATH_APPLICATION'] = 'Cthulhu'
app.config['STORMPATH_ENABLE_GIVEN_NAME'] = True
app.config['STORMPATH_ENABLE_MIDDLE_NAME'] = False
app.config['STORMPATH_ENABLE_SURNAME'] = True
app.config['STORMPATH_ENABLE_USERNAME'] = True

app.config['STORMPATH_ENABLE_FACEBOOK'] = False
app.config['STORMPATH_ENABLE_GOOGLE'] = False
app.config['STORMPATH_SOCIAL'] = {
    'FACEBOOK': {
        'app_id': FACEBOOK_APP_ID,
        'app_secret': FACEBOOK_APP_SECRET,
    },
    'GOOGLE': {
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
    }
}

'''
#Stormpath login manager
Tiene que ir antes de Los blueprints porque asigna objetos que deben renderizarse en ellos.
'''
stormpath_manager = StormpathManager(app)


from frontend.views import frontend
from api.controllers import api


app.register_blueprint(frontend)
app.register_blueprint(api)
