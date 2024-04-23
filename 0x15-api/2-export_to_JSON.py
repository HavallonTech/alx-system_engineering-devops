#!/usr/bin/python3
"""
Export to-do list to JSON Format
"""


import json
import requests
from sys import *
if __name__ == "__main__":
    # Get the employee ID from the command-line
    user_id = int(argv[1])

    url = "https://jsonplaceholder.typicode.com/"

    # get user information using the provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch the to-do list for the employee using the provided employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # ecport to a dictionary containing the user and to-do list
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # Write the data to a JSON file with the employee ID as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
