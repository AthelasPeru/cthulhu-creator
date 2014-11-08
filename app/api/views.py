#from models import user_collection, gamedata_collection
from flask import Blueprint, jsonify, request


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/v1.0/creator', methods=['GET'])
def getcharacters():
    return jsonify({"user": 2, "message": "este es tu id de pj"})
