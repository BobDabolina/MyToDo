from fastapi import FastAPI
from pymongo import MongoClient
import os
import time

app = FastAPI()
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["mytodo"]
tasks = db["tasks"]
time_on_start = time.time()


@app.get("/")
def root():
    return {"message": "Stats Service up and running!"}

@app.get("/stats")
def get_stats():
    return {
      "total_tasks": tasks.count_documents({}),
      "active_tasks": tasks.count_documents({
          "deleted": False,
          "completed": False
      }),
      "completed_tasks": tasks.count_documents({
          "completed": True,
          "deleted": False
      }),
      "deleted_tasks": tasks.count_documents({
          "deleted": True
      })
    }


@app.get("/runtime")
def get_runtime():
    return {"message": f"Time elapsed since startup: {int(time.time()) - int(time_on_start)}"}
