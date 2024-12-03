import os

import random

from prisma import Prisma
from prisma.models import User, Post, Comment

from .users import add_user, get_user, update_user, delete_user, get_users
from .posts import add_post, get_post, update_post, delete_post,  get_all_posts
from .comments import add_comment, get_comments, update_comment, delete_comment


def clear_screen() -> None:
    """Clears the console screen on both Windows and Unix-like systems."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


async def main() -> None:
    """
    Provides a simple interactive menu for interacting with the database.

    Input is requested in the form of a number, and the corresponding action is taken.
    """
    db: Prisma = Prisma()
    await db.connect()

    users: list[User] = await get_users(db)
    posts: list[Post] = await get_all_posts(db)
    comments: list[Comment] = []

    try:
        while True:
            # clear_screen()
            print("1. Create User")
            print("2. Get User")
            print("3. Get Users")
            print("4. Update User")
            print("5. Delete User")
            print("6. Create Post")
            print("7. Get Post")
            print("8. Get Posts")
            print("9. Update Post")
            print("10. Delete Post")
            print("11. Clear Screen")
            print("12. Insert Comment")
            print("13. Get Comments")
            print("14. Update Comment")
            print("15. Delete Comment")
            print("16. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                user: User = await add_user(db)
                users.append(user)

            elif choice == "2":
                # user_id = input("Enter the user ID: ")
                index = random.randint(0, len(users) - 1)
                user_id = users[index].id
                await get_user(db, user_id)

            elif choice == "3":
                users = await get_users(db)

            elif choice == "4":
                # user_id = input("Enter the user ID: ")
                index = random.randint(0, len(users) - 1)
                user_id = users[index].id
                await update_user(db, user_id)

            elif choice == "5":
                # user_id = input("Enter the user ID: ")
                index = random.randint(0, len(users) - 1)
                user_id = users[index].id
                await delete_user(db, user_id)
                users = [user for user in users if user.id != user_id]

            elif choice == "6":
                index = random.randint(0, len(users) - 1)
                user_id = users[index].id
                post = await add_post(db, user_id)
                posts.append(post)

            elif choice == "7":
                # post_id = input("Enter the post ID: ")
                index = random.randint(0, len(posts) - 1)
                post_id = posts[index].id
                await get_post(db, post_id)

            elif choice == "8":
                posts = await get_all_posts(db)

            elif choice == "9":
                # post_id = input("Enter the post ID: ")
                index = random.randint(0, len(posts) - 1)
                post_id = posts[index].id
                await update_post(db, post_id)

            elif choice == "10":
                # post_id = input("Enter the post ID: ")
                index = random.randint(0, len(posts) - 1)
                post_id = posts[index].id
                await delete_post(db, post_id)

                posts = [post for post in posts if post.id != post_id]

            elif choice == "11":
                clear_screen()

            elif choice == "12":
                # post_id = input("Enter the post ID: ")
                # user_id = input("Enter the user ID: ")
                index = random.randint(0, len(posts) - 1)
                post_id = posts[index].id
                index = random.randint(0, len(users) - 1)
                user_id = users[index].id
                comnt = await add_comment(db, post_id, user_id)
                comments.append(comnt)

            elif choice == "13":
                # post_id = input("Enter the post ID: ")
                index = random.randint(0, len(posts) - 1)
                post_id = posts[index].id
                comments = await get_comments(db, post_id)

            elif choice == "14":
                # comment_id = input("Enter the comment ID: ")
                index = random.randint(0, len(comments) - 1)
                comment_id = comments[index].id
                await update_comment(db, comment_id)

            elif choice == "15":
                # comment_id = input("Enter the comment ID: ")
                index = random.randint(0, len(comments) - 1)
                comment_id = comments[index].id
                await delete_comment(db, comment_id)

                comments = [
                    comment for comment in comments if comment.id != comment_id]

            else:
                clear_screen()
                print("Goodbye!")
                break

    finally:
        await db.disconnect()
