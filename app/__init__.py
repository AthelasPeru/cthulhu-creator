from flask import Flask
from config import DEBUG, SECRET_KEY

app = Flask(__name__)
app.config['debug'] = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY


from frontend.views import frontend
from api.controllers import api


app.register_blueprint(frontend)
app.register_blueprint(api)
