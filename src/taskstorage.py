from pymongo import MongoClient, ReturnDocument
import datetime as dt

# BASELINE
# add()
# delete()
# get()
# find()


# TODO: Turn this into external storage, separate task logic and task viewing into separate services

client = MongoClient("mongodb://localhost:27017/")
db = client["mytodo"]
task_collection = db["tasks"]
id_counter = db["id_counter"]
id_counter.update_one(
    {"_id": "task_id"},  # Find the counter
    {"$setOnInsert": {"sequence_value": 0}},  # This one stumped me, it inits the counter to 0 but only if theres a new document
    upsert=True  # Insert document if it doesnt exist
)


# Damn PyMongo is finnicky
def add_task(task, note, deadline):
    counter = id_counter.find_one_and_update(
        {"_id": "task_id"},
        {"$inc": {"sequence_value": 1}},
        return_document=ReturnDocument.AFTER
        )
    task_id = counter["sequence_value"]
    task_collection.insert_one({"id": task_id,
                                "title": task,
                                "created_at": str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                "note": None if note is None else str(note),
                                "deadline": None if deadline is None else str(deadline),
                                "completed": False,
                                "deleted": False})
    return task_id


def delete_task(task_id: int):  # Soft deletion for simplicity
    task = find_task(task_id)
    if task is not None:
        return task_collection.update_one({"id": task_id}, {"$set": {"deleted": True}})
    else:
        return None


def restore_task(task_id):
    task = find_task(task_id)
    if task is not None:
        return task_collection.update_one({"id": task_id}, {"$set": {"deleted": False}})
    else:
        return None

def get_tasks():  # All tasks
    return list(task_collection.find({}, {"_id": 0}))


def get_active():  # Only incomplete
    return list(task_collection.find({"deleted": False, "completed": False}, {"_id": 0}))


def get_deleted():  # Gets us the deleted tasks as well
    return list(task_collection.find({"deleted": True}, {"_id": 0}))


def get_completed():
    return list(task_collection.find({"completed": True}, {"_id": 0}))


def find_task(task_id):
    task = task_collection.find_one({"id": task_id}, {"_id": 0})
    if task:
        return task
    else:
        return None


def update_note(task_id, note):
    updated = task_collection.update_one(
        {"id": task_id},
        {"$set": {"note": str(note)}}
    )
    if updated.matched_count == 0:
        return None
    return updated


def update_deadline(task_id, time):  # wow code repetition!
    updated = task_collection.update_one(
        {"id": task_id},
        {"$set": {"deadline": str(time)}}
    )
    if updated.matched_count == 0:
        return None
    return updated


def complete_task(task_id):
    completed = task_collection.update_one(
        {"id": task_id},
        {"$set": {"completed": True}}
        )
    if completed.matched_count == 0:
        return None
    return completed


def uncomplete_task(task_id):
    uncompleted = task_collection.update_one(
        {"id": task_id},
        {"$set": {"completed": False}}
        )
    if uncompleted.matched_count == 0:
        return None
    return uncompleted
