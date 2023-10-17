class BookService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, book):
        return self.storage.db_add(book)

    def delete(self, id):
        self.storage.db_delete(id)

    def get(self):
        return self.storage.db_get()
