#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""

import sys
import requests


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    users_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )

    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )

    employee = requests.get(users_url).json()
    tasks = requests.get(todos_url).json()

    completed_tasks = [
        task for task in tasks if task["completed"] is True
    ]

    employee_name = employee["name"]
    completed_count = len(completed_tasks)
    total_count = len(tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            completed_count,
            total_count
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
