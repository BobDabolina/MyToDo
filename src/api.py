from fastapi import FastAPI  # This is the REST API
from fastapi import Request
from pydantic import BaseModel
import taskstorage as ts


# The goal with this is just to test FastAPI and Uvicorn
app = FastAPI()


# Pydantic base model for easy FastAPI
class CreateTask(BaseModel):
    title: str
    note: str | None = None
    deadline: str | None = None


@app.get("/")
async def root():
    return {"message:": "Hello World"}


@app.get("/tasks")
def get_tasks():
    return ts.get_tasks()


@app.get("/tasks/active")
def get_active():
    return ts.get_active()


@app.get("/tasks/deleted")
def get_deleted():
    return ts.get_deleted()


@app.get("/tasks/completed")
def get_completed():
    return ts.get_completed()


@app.post("/tasks")
def add_task(task: CreateTask):
    task_id = ts.add_task(task.title, task.note, task.deadline)
    return {"id": task_id, "message": "Task Created: ", "title": task.title}


