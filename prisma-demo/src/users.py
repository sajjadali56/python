"""
Functions for interacting with the User database.
"""

from faker import Faker

from prisma import Prisma
from prisma.models import User

from tabulate import tabulate

fake = Faker(["ar_AA", "en", "en_US", "hi_IN"])


async def add_user(db: Prisma) -> User:
    """Creates a new User in the database using faker data."""
    gender = fake.random_element(["male", "female"])
    email = fake.email()
    address = fake.address()
    full_name = fake.name() if gender == "male" else fake.name_female()

    user = await db.user.create({
        "email": email, "full_name": full_name, "gender": gender, "address": address
    })
    print("Created User", user.model_dump_json(indent=2))

    return user


async def get_user(db: Prisma, user_id: str) -> User | None:
    """Fetches a single User from the database by its ID."""
    user = await db.user.find_unique(where={"id": user_id}, include={"Post": True, "Comment": True})
    if user:
        print("Found User", user.model_dump_json(indent=2))

    return user


async def get_users(db: Prisma) -> list[User]:
    """Fetches all Users from the database."""
    users = await db.user.find_many(include={"Post": True, "Comment": True})
    # users = await db.user.find_many()
    print("Found", len(users), "users")

    data = [[user.email, user.full_name, user.gender]
            for user in users]

    print(tabulate(data, headers=["Email", "Full Name", "Gender"]))
    print()
    return users


async def update_user(db: Prisma, user_id: str) -> User | None:
    """Updates a User in the database."""
    email = fake.email()
    gender = fake.random_element(["male", "female"])
    full_name = fake.name() if gender == "male" else fake.name_female()

    user = await db.user.update(where={"id": user_id}, data={"email": email, "full_name": full_name, "gender": gender})
    if user:
        print("Updated User", user.model_dump_json(indent=2))

    return user


async def delete_user(db: Prisma, user_id: str) -> User | None:
    """Deletes a User from the database by its ID."""
    user = await db.user.delete(where={"id": user_id})
    if user:
        print("Deleted User", user.model_dump_json(indent=2))

    return user
