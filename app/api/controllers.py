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


@api.route('/v1.0/creator/<int:user_id>', methods=['GET'])
def getCharacters(user_id):
    """
    get a list of all the user Characters
    """

    _user = users_collection.find({"user_id": user_id})
    if _user.count() is 0:
        abort(404)

    for data in _user:
        try:
            characters = data['characters']
            charData = {}

            for key, character in enumerate(characters):
                
                charData.update({key +1: character})
            print "y toda mi lista {}".format(charData)
            return jsonify(charData)
        except AttributeError:
            abort(404)


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


