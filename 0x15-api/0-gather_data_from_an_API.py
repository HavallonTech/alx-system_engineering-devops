#!/usr/bin/python3
"""
 returns information about his/her TODO list progress from an API
"""

import requests
from sys import *

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    if len(argv) == 2:
        emp_id = int(argv[1])
        user_response = requests.get(url + "users/{}".format(emp_id))
        user = user_response.json()
        # Get the to-do list for the employee using the provided employee ID
        params = {"userId": emp_id}
        todos = requests.get(url + "todos", params).json()
        # Filter completed tasks and count them
        completed = [t.get("title")
                     for t in todos if t.get("completed") is True]

        # Print the employee's name and the number of completed tasks
        print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                              len(completed), len(todos)))

        # Print the completed tasks one by one with indentation
        [print("\t {}".format(complete)) for complete in completed]
