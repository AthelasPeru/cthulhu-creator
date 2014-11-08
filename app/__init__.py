from flask import Flask
from frontend.views import frontend

app = Flask(__name__)


app.register_blueprint(frontend)