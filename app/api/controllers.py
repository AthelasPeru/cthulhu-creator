#from models import user_collection, gamedata_collection
from flask import Blueprint, jsonify, request


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/v1.0/creator', methods=['GET'])
def getCharacters():
    return jsonify({"user": 2, "message": "este es tu id de pj"})


@api.route('/v1.0/creator/<int:character_id>', methods=['GET'])
def getCharacter(character_id):
    if character_id is 1:
        return jsonify({'name': 'edward wisnton'})

    else:
        return "No existe ese pj"


@api.route('/v1.0/creator/create', methods=['POST'])
def createCharacter(character_id):
	return render_template


@api.route('/v1.0/creator/<int:character_id>', methods=['PUT'])
def updateCharacter(character_id):



@api.route('/v1.0/creator/<int:character_id>', methods=['DELETE'])
def deleteCharacter(character_id):	





