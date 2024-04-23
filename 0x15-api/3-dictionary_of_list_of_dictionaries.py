#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format.

Requirements:
Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
"completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME"
ompleted": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json.
"""

import json
import requests


def fetch_user_data():
    url = "https://jsonplaceholder.typicode.com/"
    # get list of all users (employees)
    users = requests.get(url + "users").json()

    # Create a dictionary containing to-do list information of all employees
    data_to_export = {}
    for user in users:
        user_id = user["id"]
        user_url = url + f"todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
