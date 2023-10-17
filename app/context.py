from flask import g

from application.book_service import BookService
from infra.storage.mem_storage import MemoryStorage
from infra.storage.sqlite_storage import SQLiteStorage


class Context:
    def __init__(self):

        book_storage = SQLiteStorage("test.db", "book")
        self.book_service = BookService(book_storage)
        book_storage.db_create_table(["id", "title", "description", "publish_year", "pages_count", "created_at"])


def get_context(app):
    return app.config["CONTEXT"]