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
            users.append({"name": user_name, "email": user_email})
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
