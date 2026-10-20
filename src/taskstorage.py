import datetime as dt

# BASELINE
# add()
# delete()
# get()
# find()


# TODO: Turn this into external storage, separate task logic and task viewing into separate services


def add_task(tasks, task_id, task, note, deadline):
    tasks.append({"id": task_id,
                  "title": task,
                  "created_at": str(dt.datetime.now()),
                  "note": None if note is None else str(note),
                  "deadline": None if deadline is None else str(deadline),
                  "completed": False,
                  "deleted": False})
    task_id += 1
    return task_id, tasks


def delete_task(tasks, task_id):  # Soft deletion for simplicity
    task = find_task(tasks, task_id)
    if task is None:
        return tasks
    else:
        task["deleted"] = True
    return tasks


def get_tasks(tasks):  # All tasks
    return tasks


def get_active_tasks(tasks):  # Only incomplete
    active_tasks = []
    for t in tasks:
        if t["completed"] is False and t["deleted"] is False:
            active_tasks.append(t)
    return active_tasks


def get_deleted_tasks(tasks):  # Gets us the deleted tasks as well
    deleted_tasks = []
    for t in tasks:
        if t["deleted"] is True:
            deleted_tasks.append(t)
    return deleted_tasks


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_note(tasks, task_id, note):
    task = find_task(tasks, task_id)
    if task is None:
        return tasks
    task["note"] = str(note)
    return tasks


def update_deadline(tasks, task_id, time):  # Maybe I should have worked object oriented?
    task = find_task(tasks, task_id)  # SO MUCH REPETITIONS
    if task is None:
        return tasks
    task["deadline"] = str(time)
    return tasks


def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task is None:
        print(f"Couldn't find task with ID {task_id}")
    else:
        task["completed"] = True
        print(f'You Completed: {task["title"]} ')
    return tasks


def print_tasks(tasks):
    print(get_tasks(tasks))
