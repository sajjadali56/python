import pickle
from dataclasses import dataclass


@dataclass
class User:
    """User dataclass"""
    name: str
    age: int
    job: str
    city: str
    country: str
    hobbies: list
    favorite_color: str
    favorite_number: int
    favorite_movie: str


data: list[User] = [
    User(
        name="John",
        age=30,
        job="Engineer",
        city="New York",
        country="USA",
        hobbies=["Reading", "Playing video games"],
        favorite_color="Blue",
        favorite_number=7,
        favorite_movie="The Matrix",
    ),
    User(
        name="Jane",
        age=25,
        job="Designer",
        city="London",
        country="UK",
        hobbies=["Drawing", "Listening to music"],
        favorite_color="Red",
        favorite_number=3,
        favorite_movie="The Avengers",
    ),
]

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    data = pickle.load(f)

print(data[0].name)
