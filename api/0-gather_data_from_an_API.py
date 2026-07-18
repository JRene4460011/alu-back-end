#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )

    employee = requests.get(user_url).json()
    tasks = requests.get(todos_url).json()

    completed_tasks = [
        task for task in tasks if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee.get("name"),
            len(completed_tasks),
            len(tasks)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
