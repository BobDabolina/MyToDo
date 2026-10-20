import taskstorage as ts


tasks = []
next_id = 1
next_id, tasks = ts.add_task(tasks, next_id, "Buy Food")
next_id, tasks = ts.add_task(tasks, next_id, "Get Food")

print(ts.get_tasks(tasks))
print(ts.find_task(tasks, 2))
print(ts.find_task(tasks, 3))
tasks = ts.complete_task(tasks, 2)
tasks = ts.complete_task(tasks, 3)
print(ts.get_tasks(tasks))
tasks = ts.delete_task(tasks, 2)
ts.print_tasks(tasks)
