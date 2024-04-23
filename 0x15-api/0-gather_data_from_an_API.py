#!/usr/bin/python3
"""
 returns information about his/her TODO list progress from an API
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(emp_id))
    user = user_response.json()
    params = {"userid": emp_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    completed = []
    for data in todos:
        if data.get("completed") is True:
            completed.append(data.get("title"))
    print("Employee {} is done with tasks({}/{}".format(user.get("name"),
          len(completed), len(todos)))
    for complete in completed:
        print("\t {}".format(complete))
