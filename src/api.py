from fastapi import FastAPI  # This is the REST API
from fastapi import HTTPException
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
    return {"message:": "Did you forget [python -m uvicorn api:app --reload] again? :P"}


# TASK CREATIONS
@app.post("/tasks")
def add_task(task: CreateTask):
    task_id = ts.add_task(task.title, task.note, task.deadline)
    return {"id": task_id, "message": "Task Created: ", "title": task.title}


@app.patch("/tasks/{task_id}/restore")
def restore_task(task_id: int):
    result = ts.restore_task(task_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )
    return {"message": f"Task {task_id} restored!"}


@app.get("/tasks")
def get_tasks():
    return ts.get_tasks()


@app.get("/tasks/active")
def get_active():
    return ts.get_active()


# TASK DELETIONS
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    result = ts.delete_task(task_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )
    return {"message": f"Task {task_id} deleted!"}


@app.get("/tasks/deleted")
def get_deleted():
    return ts.get_deleted()


# TASK COMPLETIONS
@app.get("/tasks/completed")
def get_completed():
    return ts.get_completed()


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    result = ts.complete_task(task_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )        
    return {"message": f"Task {task_id} completed!"}


@app.patch("/tasks/{task_id}/incomplete")
def undo_completion(task_id: int):
    result = ts.uncomplete_task(task_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )
    return {"message": f"Task {task_id} marked as incomplete!"}




