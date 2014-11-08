import pymongo

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

# profesiones
proffessions_collection = db.proffessions

# items
items_collection = db.items

# skills
skills_collection = db.skills

# languages
languages_collection = db.languages

# spells
spells_collection = db.spells

# books
books_collection = db.books


if proffessions_collection.count() 

print books_collection.count()
