import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Control_de_libros"]
collection = db["Libros"]

print(collection)
