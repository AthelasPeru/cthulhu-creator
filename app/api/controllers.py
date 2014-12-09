# from models import user_collection, gamedata_collection
from flask import Blueprint, jsonify, request, abort, make_response
from models import users_collection, gamedata_collection

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/v1.0/character/rules/<string:rules>', methods=['GET'])
def getRulesData(rules):
    """
    Get the data for specific rule set
    """
    print "got a connection"
    rulesData = gamedata_collection.find({"version": rules})
    if rulesData.count() is 0:
        abort(404)
    for data in rulesData:

        return jsonify(data)


@api.route('/v1.0/character/<int:user_id>', methods=['GET'])
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

                charData.update({key: character})
            return jsonify(charData)
        except AttributeError:
            abort(404)


@api.route('/v1.0/character/<int:user_id>/<int:character_id>', methods=['GET'])
def getCharacter(user_id, character_id):
    """
    Get the data of a single character
    """
    _user = users_collection.find({"user_id": user_id})

    characterData = {}

    if _user.count() is 0:
        abort(404)
    for data in _user:
        try:
            character = data["characters"][character_id]
            return jsonify(character)
        except AttributeError:
            abort(404)


@api.route('/v1.0/character/<int:user_id>', methods=['POST'])
def addCharacter(user_id):
    """
    add a new character, it requires the id as well
    """
    # este se puede cambiar por jsen si es que lo mandan en json
    if not request.json:
        abort(400)

    characterData = request.json["character"]
    try:
        users_collection.update({"user_id": user_id}, {
            '$push': {
                "characters": characterData
            }
        })

        return jsonify({"status": "Character Saved"})
    except:
        return jsonify({"status": "An error occured, sorry!!!"}), 500


@api.route('/v1.0/character/<int:user_id>/<int:character_id>', methods=['PUT'])
def updateCharacter(user_id, character_id):
    """
    Update the data for a character
    """

    characterData = request.json["character"]
    if not request.json:
        abort(400)
    try:
        users_collection.update(
            {"user_id": user_id, "characters.id": character_id},
            {"$set": {"characters.$": characterData}}

        )
        return jsonify({"status": "character updated"})
    except:
        return jsonify({"status": "An error occured, sorry!!!"}), 500


@api.route('/v1.0/character/<int:user_id>/<int:character_id>', methods=['DELETE'])
def deleteCharacter(user_id, character_id):
    """
    Delete a specific character
    """
    try:

        users_collection.update(
            {"user_id": user_id}, {"$pull": {"characters": {"id": character_id}}})

        return jsonify({"status": "Character Deleted"})
    except:
        return jsonify({"status": "An error occured, sorry!!!"}), 500


# error handlers
@api.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@api.errorhandler(403)
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@api.errorhandler(401)
def not_allowed(error):
    return make_response(jsonify({'error': 'Access Restricted'}), 401)


