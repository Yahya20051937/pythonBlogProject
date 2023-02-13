import queue
import sqlite3

import tkinter as tk
from tkinter import ttk
from types import coroutine

q1 = queue.Queue()
q = queue.Queue()
q2 = queue.Queue()
q3 = queue.Queue()


@coroutine
def add_comment():
    from DATABASE.database import DatabaseManagement, BlogDatabase
    from main import logger
    try:
        with DatabaseManagement('blog_database.db') as connection:
            database = BlogDatabase(connection)
            while True:
                try:
                    user, post_id, text_area, button3, button = yield
                    print(user, post_id, text_area, button3, button, 3)
                except StopIteration:
                    pass
                # button.destroy()
                content = text_area.get("1.0", "end-1c")
                database.add_comment(post_id, content, user)
                text_area.destroy()

                button3.pack(side='top')
    except sqlite3.ProgrammingError:
        print(911)


async def add_comment_async(g):
    await g


@coroutine
def add_like():
    from DATABASE.database import DatabaseManagement, BlogDatabase
    try:
        with DatabaseManagement('blog_database.db') as connection:
            database = BlogDatabase(connection)
            while True:
                post_id, like_button, liked_button, frame2 = yield
                print(4)
                database.add_like(post_id)
                like_button.destroy()
                frame2.pack(side='left', fill='x', expand=True)
                liked_button.pack(side='right', fill='x', expand=True)
    except sqlite3.ProgrammingError:
        print(912)


async def add_like_async(g):
    await g


def get_comments_users(post_id):
    from main import logger
    from DATABASE.database import DatabaseManagement, BlogDatabase
    with DatabaseManagement('blog_database.db') as connection:
        database = BlogDatabase(connection)
        comments_data = database.get_columns_data(post_id, 'comments')
        all_data = []

        sep_comments = comments_data[0].split(',')
        logger.debug(f'sep comments : {sep_comments}')
        for co in sep_comments[:-1]:
            data = co.split('//')

            comment = data[0]
            user = data[1]
            all_data.append((comment, user))

    return all_data


def send_data(*args, func):
    try:
        func.send(args)
        print(args)
    except StopIteration:
        print(args)








