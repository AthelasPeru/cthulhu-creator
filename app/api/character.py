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
users_collection = db.users

data = {
    "characters": {
        "id": 1,
        "general_data":
            {
                "complete_name": "",
                "profession": "",
                "degree": "",
                "birthplace": "",
                "mental_disorde": "",
                "gender": "",
                "age": ""
            },
    }
}


users_collection.update({"user_id": 1}, {"$push": {
    "characters": {
        "id":3,
        "general_data":
            {
                "complete_name": "Polo",
                "profession": "",
                "degree": "",
                "birthplace": "",
                "mental_disorde": "",
                "gender": "",
                "age": ""
            },
    }
}})
