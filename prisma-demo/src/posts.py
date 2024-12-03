"""Functions for interacting with the Post database."""

from prisma import Prisma
from prisma.models import Post

from tabulate import tabulate

from .users import fake


async def add_post(db: Prisma, user_id: str) -> Post:
    """Creates a new Post in the database using faker data.
    Args:
        db (Prisma): The Prisma client instance.
    Returns:
        Post: The newly created Post.
    """
    title = fake.sentence()
    desc = fake.text()
    published = fake.boolean()

    post = await db.post.create(
        {
            "user_id": user_id,
            "title": title,
            "desc": desc,
            "published": published,
        }
    )

    print("Created Post", post.model_dump_json(indent=2))

    return post


async def get_all_posts(db: Prisma) -> list[Post]:
    """Fetches all Posts from the database.
    Args:
        db (Prisma): The Prisma client instance.
    Returns:
        list[Post]: A list of Post objects.
    """
    posts = await db.post.find_many(include={"Comment": True})
    print("Found", len(posts), "posts")

    data = [[post.title, post.desc, post.published]
            for post in posts]

    print(tabulate(data, headers=[
          "Title", "Description", "Published"]))

    # for post in posts:
    #     print(post.model_dump_json(indent=2))

    return posts


async def get_posts(db: Prisma, user_id: str) -> list[Post]:
    """Fetches all Posts from the database.
    Args:
        db (Prisma): The Prisma client instance.
    Returns:
        list[Post]: A list of Post objects belonging to the given User.
    """
    posts = await db.post.find_many(where={"user_id": user_id}, include={"Comment": True})
    print("Found", len(posts), "posts")

    for post in posts:
        print(post.model_dump_json(indent=2))

    return posts


async def get_post(db: Prisma, post_id: str) -> Post | None:
    """Fetches a single Post from the database by its ID.
    Args:
        db (Prisma): The Prisma client instance.
        id (str): The unique identifier of the Post to retrieve.
    Returns:
        Post: The Post object corresponding to the given ID.
    """
    post = await db.post.find_unique(where={"id": post_id}, include={"Comment": True})
    if post:
        print("Found Post", post.model_dump_json(indent=2))

    return post


async def update_post(db: Prisma, post_id: str) -> Post | None:
    """Updates a Post in the database.
    Args:
        db (Prisma): The Prisma client instance.
        id (str): The unique identifier of the Post to update.
    Returns:
        Post: The updated Post object.
    """
    title: str = fake.sentence()
    desc: str = fake.text()
    published: bool = fake.boolean()

    post = await db.post.update(
        where={"id": post_id},
        data={"published": published, "title": title, "desc": desc},

    )

    if post:
        print("Updated Post", post.model_dump_json(indent=2))

    return post


async def delete_post(db: Prisma, id: str) -> Post | None:
    """Deletes a Post from the database by its ID.
    Args:
        db (Prisma): The Prisma client instance.
        id (str): The unique identifier of the Post to delete.
    Returns:
        Post: The deleted Post object.
    """
    post = await db.post.delete(where={"id": id})
    if post:
        print("Deleted Post", post.model_dump_json(indent=2))

    return post
