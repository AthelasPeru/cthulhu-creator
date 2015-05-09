import pymongo

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

data = {
	"version": "5.0",
	"description": "this is a really popular rules set"
}

rules_set.insert(data)