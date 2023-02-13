import sqlite3 as sql3

from random import randint
from datetime import datetime


class DatabaseManagement:
    def __init__(self, file):
        self.connection = None
        self.file = file

    def __enter__(self):
        self.connection = sql3.connect(self.file, check_same_thread=False)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_type:
            self.connection.commit()
            self.connection.close()

        self.connection.commit()
        self.connection.close()


class Database:
    def __init__(self, connection):
        self.name = None
        self.connection = connection
        self.cursor = self.connection.cursor()


class UserDatabase(Database):
    def __init__(self, connection):
        super().__init__(connection)
        self.name = 'user_database'

    def create_table(self):
        self.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.name} (username text, email text, password text, log text)')

    def add_user(self, user_data):
        self.cursor.execute(f'INSERT INTO {self.name} VALUES(?,?,?,?)',
                            (user_data[0], user_data[1], user_data[2], user_data[3]))


class BlogDatabase(Database):
    def __init__(self, connection):
        super().__init__(connection)
        self.name = 'blog_database'

    def create_table(self):
        self.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.name} (post_id int,'
            f'blog_time text,blog text,user text,likes int,comments text,commentsn int ,shares int)')

    def add_post(self, blog, user, post_id=randint(0, 100000000000000)):
        self.cursor.execute(f'INSERT INTO {self.name} VALUES(?,?,?,?,?,?,?,?)',
                            (post_id, str(datetime.today())[:-10], blog, user, 0, '', 0, 0))

    def get_all_posts(self):
        from main import logger
        self.cursor.execute(f'SELECT * FROM {self.name}')
        posts = [i for i in self.cursor.fetchall()]
        logger.debug(f'all posts : {posts}')
        return posts

    def add_like(self, post_id):
        from main import logger
        self.cursor.execute(f'SELECT likes FROM {self.name} WHERE post_id = ?', (post_id,))
        likes = self.cursor.fetchall()[0][0]
        logger.debug(f'likes: {likes}')
        self.cursor.execute(f'UPDATE {self.name} SET likes = ? WHERE post_id = ?', (likes + 1, post_id))

    def add_comment(self, post_id, comment, user):
        from main import logger
        self.cursor.execute(f'SELECT comments, commentsn FROM {self.name} WHERE post_id = ?', (post_id,))

        data = self.cursor.fetchall()[0]

        comments = data[0]
        commentsn = data[1]
        logger.debug(f'comments : {comments}, {commentsn}')
        self.cursor.execute(f'UPDATE {self.name} SET comments = ? WHERE post_id = ?',
                            (comments + f'{comment}//{user},', post_id))

        self.cursor.execute(f'UPDATE {self.name} SET commentsn = ? WHERE post_id = ?', (commentsn + 1 , post_id))

    def get_columns_data(self, post_id, columns):
        from main import logger
        self.cursor.execute(f'SELECT {columns} FROM {self.name} WHERE post_id = ?', (post_id, ))
        data = [i[0] for i in self.cursor.fetchall()]
        logger.debug(f'all data: {data}')
        return data



