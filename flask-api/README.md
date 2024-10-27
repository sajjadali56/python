# Rest Api with Flask Library

## HTTP Request methods

- GET: getting the data in json format
- PUT: Used to update the object at the server
- PATCH: used to partially update the data
- POST: used to create or append data
- DELETE: used to delete the data

## Python Code

### server.py

```python
from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

CSV_FILE = 'data.csv'
users = []

def read_users():
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def write_users(local_users):
    with open(CSV_FILE, 'w', newline='') as file:
        headers = ['id', 'name', 'email']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(local_users)

def append_user(user):
    with open(CSV_FILE, 'a', newline='') as file:
        headers = ['id', 'name', 'email']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerow(user)

users = read_users()

"""
Description: This is a simple API for managing users
REST API: 
    - GET /users/: Get all users
    - POST /users/: Create a new user
    - GET /users/<int:user_id>/: Get user by id
    - PUT /users/<int:user_id>/: Update user by id
    - DELETE /users/<int:user_id>/: Delete user by id
"""
@app.route('/users/', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/', methods=['POST'])
def create_user():
    user = request.json
    new_uers = {
        'id': int(users[-1]["id"]) + 1 if users else 1,
        'name': user['name'],
        'email': user['email']
    }
    users.append(new_uers)
    append_user(new_uers) if len(users) > 1 else write_users(users)
    return jsonify(user), 201 # 201 Created status code

@app.route('/users/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    for x in users:
        if x['id'] == str(user_id):
            return jsonify(x), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>/', methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = request.json
    for x in users:
        if x['id'] == user_id:
            x['name'] = user['name']
            x['email'] = user['email']
            write_users(users)
            return jsonify(x), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    for x in users:
        if x['id'] == str(user_id):
            users.remove(x)
            write_users(users)
            return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Client App

```python
import http
import requests

"""
Add the user by sending a POST request to the server with the user name and email
Server URL: http://localhost:5000/users/
Server Method: POST
Request Headers: Content-Type: application/json
Request Body: {"name": "", "email": ""}
Response: user object with fields id, name, and email! 201 Created
"""

API = "http://localhost:5000/users/"
def add_user(user_name, user_email):
    obj = {
        "name": user_name,
        "email": user_email
    }

    res = requests.post(API, json=obj)
    if res.status_code == http.HTTPStatus.CREATED:
        print(res.json())
    else:
        print("User not created")

def get_user(id):
    res = requests.get(f"{API}{id}/")
    if res.status_code == http.HTTPStatus.OK:
        print(res.json())
    else:
        print("User not found")

def update_user(id, user_name, user_email):
    obj = {
        "name": user_name,
        "email": user_email
    }

    res = requests.put(f"{API}{id}/", json=obj)
    if res.status_code == http.HTTPStatus.OK:
        print(res.json())
    else:
        print("User not updated")

def delete_user(id):
    res = requests.delete(f"{API}{id}/")
    if res.status_code == http.HTTPStatus.OK:
        print(res.json())
    else:
        print("User not deleted")

def get_all_users():
    res = requests.get(API)
    if res.status_code == http.HTTPStatus.OK:
        print(res.json())
    else:
        print("No user found")

ADD_USER = 1
GET_USER = 2
UPDATE_USER = 3
DELETE_USER = 4
GET_ALL_USERS = 5
EXIT = 6

choices = """
Type Any Number in the menue for preferred operation:
1. Add the user
2. Get the user
3. Update the user
4. Delete the user
5. Get all users
6. Exit

    """

def main():
    users = []
    while True:
        print(choices)
        choice = int(input("Enter your choice: "))
        if choice == ADD_USER:
            user_name = input("Enter the user name: ")
            user_email = input("Enter the user email: ")
            add_user(user_name, user_email)
        elif choice == GET_USER:
            user_id = int(input("Enter the user id: "))
            get_user(user_id)
        elif choice == UPDATE_USER:
            user_id = int(input("Enter the user id: "))
            user_name = input("Enter the user name: ")
            user_email = input("Enter the user email: ")
            update_user(user_id, user_name, user_email)
        elif choice == DELETE_USER:
            user_id = int(input("Enter the user id: "))
            delete_user(user_id)
        elif choice == GET_ALL_USERS:
            get_all_users()
        elif choice == EXIT:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
```