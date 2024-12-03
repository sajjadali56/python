"""
Functions for interacting with the Comment database.
"""

from prisma import Prisma
from prisma.models import Comment

from .users import fake


async def get_comments(db: Prisma, post_id: str) -> list[Comment]:
    """Fetches all Comments from the database.
    Args:
        db (Prisma): The Prisma client instance.
    Returns:
        list[Comment]: A list of Comment objects of the given Post.
    """

    comments = await db.comment.find_many(where={"post_id": post_id}, order={"created_at": "desc"})
    print("Found", len(comments), "comments for Post", post_id)

    for comment in comments:
        print(comment.model_dump_json(indent=2))

    return comments


async def add_comment(db: Prisma, post_id: str, user_id: str) -> Comment:
    """Creates a new Comment in the database using faker data.
    Args:
        db (Prisma): The Prisma client instance.
        post_id (str): The unique identifier of the Post to which the Comment belongs.
    Returns:
        Comment: The newly created Comment.
    """

    content = fake.text()
    comment = await db.comment.create({"content": content,  'post_id': post_id, 'user_id': user_id}, include={"post": True})
    print("Created Comment", comment.model_dump_json(indent=2))

    return comment


async def delete_comment(db: Prisma, id: str) -> Comment | None:
    """Deletes a Comment from the database by its ID.
    Args:
        db (Prisma): The Prisma client instance.
        id (str): The unique identifier of the Comment to delete.
    Returns:
        Comment: The deleted Comment object.
    """

    comment: Comment | None = await db.comment.delete(where={"id": id})
    if comment:
        print("Deleted Comment", comment.model_dump_json(indent=2))

    return comment


async def update_comment(db: Prisma, id: str) -> Comment | None:
    """Updates a Comment in the database.
    Args:
        db (Prisma): The Prisma client instance.
        id (str): The unique identifier of the Comment to update.
    Returns:
        Comment: The updated Comment object.
    """
    content = fake.text()

    comment = await db.comment.update(
        where={"id": id},
        data={"content": content},
    )

    if comment:
        print("Updated Comment", comment.model_dump_json(indent=2))

    return comment
