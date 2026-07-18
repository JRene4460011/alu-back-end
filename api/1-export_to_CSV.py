#!/usr/bin/python3
"""Module that exports an employee's TODO list progress to CSV."""

import csv
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
 
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
