from flask import Flask, render_template, request
import tkinter as tk


class Flask__:
    app = Flask(__name__)

    @classmethod
    def run(cls):
        cls.app.run(port=5003, debug=False)

    @staticmethod
    @app.route('/')
    def home_page():
        from main import logger
        from DATABASE.database import DatabaseManagement, BlogDatabase
        with DatabaseManagement('blog_database.db') as connection:
            database = BlogDatabase(connection)
            posts = database.get_all_posts()
            logger.debug(f'all data : {posts}')
        return render_template('home.html', posts=posts)

    @staticmethod
    @app.route('/like_post', methods=['POST', 'GET'])
    def like_post():
        from main import logger
        from DATABASE.database import DatabaseManagement, BlogDatabase
        with DatabaseManagement('blog_database.db') as connection:
            database = BlogDatabase(connection)
            post_id = list(request.args.keys())[0]
            database.add_like(post_id)
        return Flask__.home_page()

    @staticmethod
    @app.route('/comment_on_post')
    def comment_on_post():
        from posts_management.post_interactions import comment_on_post_gui
        post_id = list(request.args.keys())[0]
        comment_on_post_gui('yahya_05', post_id)
        return Flask__.home_page()

    @staticmethod
    @app.route('/interact_gui')
    def interact_gui():
        post_id = list(request.args.keys())[0]


