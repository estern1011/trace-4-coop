from pymongo import MongoClient

client = MongoClient("localhost", 27017)

if "review_store" in client.list_database_names():
    client.drop_database("review_store")

db = client.review_store
db.create_collection("companies")
db.create_collection("job_postings")
db.create_collection("reviews")