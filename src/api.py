from fastapi import FastAPI  # This is the REST API
from fastapi import Request
from pydantic import BaseModel
import taskstorage as ts


# The goal with this is just to test FastAPI and Uvicorn

app = FastAPI()
tasks = []
next_id = 1

next_id, tasks = ts.add_task(tasks, next_id, "Buy Food", None, None)
next_id, tasks = ts.add_task(tasks, next_id, "Get Food", None, None)


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
    return ts.get_tasks(tasks)


@app.post("/tasks")
def add_task(task: CreateTask):
    global next_id, tasks  # Lmao I forgot that there were local variables
    next_id, tasks = ts.add_task(tasks, next_id, task.title, task.note, task.deadline)
    return next_id, tasks
