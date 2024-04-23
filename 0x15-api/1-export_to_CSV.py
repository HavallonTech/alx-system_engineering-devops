#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the CSV format.
"""


import csv
import requests
from sys import *
if __name__ == "__main__":
    # Get the user ID from the command-line arguments
    user_id = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from API
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract the username from the user data
    username = user.get("username")

    """Fetch the to-do list items associated with the
    given user ID and convert the response to a JSON object
    """
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    """Use list comprehension to iterate over the to-do list items
     write each item's details (user ID, username, completion status,
    """
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
