from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from tabulate import tabulate
from faker import Faker

import platform
import os

from student import Student, BASE, engine

fake = Faker()


SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()


def clear_screen():
    """
    Clears the terminal screen based on the operating system.
    Uses 'cls' command for Windows and 'clear' command for Linux/Unix/Mac.
    """
    if platform.system() == "Windows":
        os.system("cls")  # Clear screen for Windows
    else:
        os.system("clear")  # Clear screen for Linux/Unix/Mac


# Example usage
clear_screen()


def add_student(name: str, age: int, gender: str) -> Student:
    """
    Adds a new student to the database.

    Args:
        name (str): The student's name.
        age (int): The student's age.
        gender (str): The student's gender.

    Returns:
        Student: The newly created student object.
    """
    std = Student(name=name, age=age, gender=gender)
    session.add(std)
    session.commit()

    return std


def get_student(id: int) -> Student:
    """
    Retrieves a student from the database by their ID.

    Args:
        id (int): The ID of the student to retrieve.

    Returns:
        Student: The student object if found; otherwise, None.
    """
    return session.query(Student).where(Student.id == id).first()


def update_student(id: int, name: str, age: int, gender: str) -> Student:
    """
    Updates a student in the database.

    Args:
        id (int): The ID of the student to update.
        name (str): The new name of the student.
        age (int): The new age of the student.
        gender (str): The new gender of the student.

    Returns:
        Student: The updated student object.
    """
    std = session.query(Student).where(Student.id == id).first()
    std.name = name
    std.age = age
    std.gender = gender
    session.commit()

    return std


def delete_student(id: int) -> Student:
    """
    Deletes a student from the database by their ID.

    Args:
        id (int): The ID of the student to delete.

    Returns:
        Student: The deleted student object.
    """
    std = session.query(Student).where(Student.id == id).first()
    session.delete(std)
    session.commit()

    return std


def get_all_students() -> list[dict[str, str | int]]:
    """
    Retrieves all students from the database.

    Returns:
        list[dict[str, str | int]]: A list of dictionaries, each representing
        a student with keys "id", "name", "age", and "gender".
    """
    results = session.query(Student).all()
    data = [std.to_dict() for std in results]
    return data


while True:
    print("1. Add student")
    print("2. Get student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Get all students")
    print("6. Clear screen")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        gender = fake.random_element(elements=("Male", "Female"))
        name = fake.name() if gender == "Male" else fake.name_female()
        age = fake.random_int(min=16, max=100)
        res = add_student(name, age, gender)
        print(res)
    elif choice == "2":
        id = input("Enter id: ")
        res = get_student(id)
        print(res)
    elif choice == "3":
        id = input("Enter id: ")
        gender = fake.random_element(elements=("Male", "Female"))
        name = fake.name() if gender == "Male" else fake.name_female()
        age = fake.random_int(min=16, max=100)
        res = update_student(id, name, age, gender)
        print(res)
    elif choice == "4":
        id = input("Enter id: ")
        res = delete_student(id)
        print(res)
    elif choice == "5":
        res = get_all_students()
        print(tabulate(res, headers="keys"))
    elif choice == "6":
        clear_screen()
    elif choice == "7":
        break


session.close()

engine.dispose()
