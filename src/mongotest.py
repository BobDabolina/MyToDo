from pymongo import MongoClient

# Could honestly change this for security, but its localhost so...
client = MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())

db = client["mytodo"]
db.mytodo.insert_one({"title": "DB TEST"})
print(list(db.mytodo.find()))