import pymongo
import os
import json
from config import LOAD_DATA, DROP_DATA

# Connection to Mongo DB
try:
    conn = pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure as e:
    print "Could not connect to MongoDB: {}}".format(e)


# create and connect to the database
db = conn.cthulhu

# create and select collections

# usuarios
users_collection = db.users

gamedata_collection = db.gamedata


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
JSON_URL = os.path.join(SITE_ROOT, "json_data/")

# delete the Db if the config says so
if DROP_DATA:
    db.drop_collection("gamedata")

# add data to the Database
if LOAD_DATA:

    # Si el config load es True
    with open(JSON_URL + "static_data.json") as data:
        gamedata = json.loads(data.read())

        # Load all the static data
        gamedata_collection.insert(gamedata)
