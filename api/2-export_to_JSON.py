#!/usr/bin/python3
"""Module that exports an employee's TODO list progress to JSON."""

import json
import sys
 
import requests
 
 
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
 
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos".format(base_url)
 
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")
 
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos_data = todos_response.json()
 
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos_data
    ]
 
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)
