import sqlite3

from app.domain.book import Book


class SQLiteStorage:
    def __init__(self, db_name, table_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.table_name = table_name
        self.id = 0

    def db_create_table(self, columns):
        query = f"CREATE TABLE {self.table_name} ({', '.join(columns)})"
        self.cursor.execute(query)

    def db_add(self, book):
        self.id += 1
        query = f"INSERT INTO {self.table_name}('id', 'title', 'description', 'publish_year', 'pages_count', 'created_at') VALUES({self.id}, '{book.title}', '{book.description}', {book.publish_year}, {book.pages_count}, date('{book.created_at}'))"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
        return self.id

    def db_delete(self, id):
        pass

    def db_get(self):
        query = f"SELECT * FROM {self.table_name}"
        all_books = self.cursor.execute(query)

        return list(map(lambda x: Book(x[1], x[2], x[3], x[4], x[5]), all_books.fetchall()))
