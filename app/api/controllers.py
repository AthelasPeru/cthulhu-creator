#from models import user_collection, gamedata_collection
from flask import Blueprint, jsonify, request, abort, make_response
from models import users_collection, gamedata_collection

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/v1.0/creator/rules/<string:rules>', methods=['GET'])
def getRulesData(rules):
    """
    Get the data for specific rule set
    """

    rulesData = gamedata_collection.find({"version": rules})
    if rulesData.count() is 0:
        abort(404)
    for data in rulesData:

        return jsonify(data)


@api.route('/v1.0/creator', methods=['GET'])
def getCharacters():
    """
    get a list of all the users getCharacters
    """

    return jsonify({"user": 2, "message": "este es tu id de pj"})


@api.route('/v1.0/creator/<int:character_id>', methods=['GET'])
def getCharacter(character_id):
    """
    Get the data of a single character
    """

    characterData = users_collection.find({"_id": character_id})
    if characterData.count() is 0:
        abort(404)
    for data in characterData:
        return jsonify(data)


@api.route('/v1.0/creator/save/<int:character_id>', methods=['POST'])
def saveCharacter(character_id):
    """
    Save a new character
    """

    return "create"


@api.route('/v1.0/creator/<int:character_id>', methods=['PUT'])
def updateCharacter(character_id):
    """
    Update the data for a character
    """
    return "good bye"


@api.route('/v1.0/creator/<int:character_id>', methods=['DELETE'])
def deleteCharacter(character_id):
    """
    Delete a specific character
    """
    return "hello"


# error handlers
@api.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@api.errorhandler(401)
def not_allowed(error):
    return make_response(jsonify({'error': 'Access Restricted'}), 401)
