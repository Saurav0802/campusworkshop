"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq5jhmbg5e4khqqhv0-a",
        database="todo_f0jw",
        user="root",
        password="R9g6cAvs658eIYZY2IWsV9troncSxkUF")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
