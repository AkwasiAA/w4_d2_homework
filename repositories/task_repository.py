from db.run_sql import run_sql
from models.task import Task
from repositories.user_repository import *

# READ-ALL
def select_all():
    tasks = []
    # create a sql statement

    sql = "SELECT * FROM tasks"
    # execute sql statement
    # get results
    # list of dicts:
    results = run_sql(sql)

    for row in results:
        task = Task(
            row["description"], 
            row["assignee"], 
            row["duration"], 
            row["completed"], 
            row["id"]
            )
        tasks.append(task)

    # I want to get a list of Task objects
    return tasks

# CREATE
def save(task):
    # sql = f"INSERT INTO tasks (description, assignee, duration, completed) VALUES ('{task.description}', '{task.assignee}', {task.duration}, {task.completed})"
    sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [task.description, task.user.idg, task.duration, task.completed]
    # protect against sql query inject attacks (values are inserted into %s postions in exact order that we have entered them)
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task

# READ-ONE
def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id  = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        task = Task(result['description'], result['user'], result['duration'], result['completed'], result['id'])
        # this is essentially returning the headers of the table we have in our database
    return task

# DELETE-ALL
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)

# DELETE-ONE
def delete_one(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
def update(task):
    sql = "UPDATE tasks SET (description, assignee, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    # pass in all objected because you never know which parts you'll want to update
    values = [task.description, task.assignee, task.duration, task.completed, task.id]
    run_sql(sql, values)


