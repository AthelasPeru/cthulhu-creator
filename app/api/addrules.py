import pymongo
import json

try:
    conn = pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure as e:
    print "Could not connect to MongoDB: {}}".format(e)


# create and connect to the database
db = conn.cthulhu

# create and select collections

# usuarios
rules_set = db.rules_set

with open("rules.json") as rules:
	data = rules.read()
	new_rules =  json.loads(data)

	rules_set.insert(new_rules)