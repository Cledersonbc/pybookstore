import json
import os

from pybookstore import BASE_DIR
from pybookstore.models import Book
from pybookstore.schemas import BookSchema


def read_example():
    try:
        path = os.path.join(BASE_DIR, 'example', 'books.json')
        with open(path) as json_data:
            return json.load(json_data)
    except FileNotFoundError as e:
        print('%s: %s' % (e.strerror, e.filename))
        return None


def read_all():
    """
    URL: /api/books
    :return: a list of books
    """
    books = Book.query.all()
    book_schema = BookSchema(many=True)
    if books is not None:
        return book_schema.jsonify(books)

    return None


def read(book_id):
    """
    URL: /api/books/{book_id}
    :return: a book (if found) by ID
    """
    book = Book.query.get(book_id)
    book_schema = BookSchema()
    if book is not None:
        return book_schema.dump(book).data

    return None
