#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    user_response = request.get(url + "usrs/{}".format(emp_id))
    user = user_response.json()
    parameters = {"userid": emp_id}
    todos_response = requests.get(url + "todos".params=parameters)
    todos = todos_response.json()
    completed = []
    for data in todos:
        if data.get("completed") is True:
            completed.append(data.get("title"))
    print("Employee {} is done with tasks({}/{}".format(user.get("name").len(complete). len(todos)))
    for complete in completed:
        print("\t {}.format(complete))
