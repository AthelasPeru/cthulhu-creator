from flask import Flask

from config import config
from extensions import stormpath_manager, debugtoolbar


# app.config['STORMPATH_API_KEY_FILE'] = STORMPATH_API_KEY_FILE
# app.config['STORMPATH_REDIRECT_URL'] = '/'
# app.config['STORMPATH_APPLICATION'] = 'Cthulhu'
# app.config['STORMPATH_ENABLE_GIVEN_NAME'] = True
# app.config['STORMPATH_ENABLE_MIDDLE_NAME'] = False
# app.config['STORMPATH_ENABLE_SURNAME'] = True
# app.config['STORMPATH_ENABLE_USERNAME'] = True

# app.config['STORMPATH_ENABLE_FACEBOOK'] = False
# app.config['STORMPATH_ENABLE_GOOGLE'] = False
# app.config['STORMPATH_SOCIAL'] = {
#     'FACEBOOK': {
#         'app_id': FACEBOOK_APP_ID,
#         'app_secret': FACEBOOK_APP_SECRET,
#     },
#     'GOOGLE': {
#         'client_id': GOOGLE_CLIENT_ID,
#         'client_secret': GOOGLE_CLIENT_SECRET,
#     }
# }



'''
#Stormpath login manager
Tiene que ir antes de Los blueprints porque asigna objetos que deben renderizarse en ellos.
'''



from frontend.views import frontend
from api.controllers import api



def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    # stormpath_manager.init_app(app)
    debugtoolbar.init_app(app)
    
    app.register_blueprint(frontend)
    app.register_blueprint(api)

    return app