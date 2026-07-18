#!/usr/bin/python3
"""Module that exports data for all employees in JSON format."""

import json 
import requests
 
 
if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
 
    users_response = requests.get("{}/users".format(base_url))
    users_data = users_response.json()
 
    todos_response = requests.get("{}/todos".format(base_url))
    todos_data = todos_response.json()
 
    all_employees = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data
            if task.get("userId") == user_id
        ]
        all_employees[str(user_id)] = user_tasks
 
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees, json_file)
