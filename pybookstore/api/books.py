import json
import os

from marshmallow import ValidationError

from pybookstore import BASE_DIR
from pybookstore import db
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


def create(book):
    """
    URL: /api/books
    :return: a book (if created) with ID
    """
    try:
        book_schema = BookSchema(strict=True)
        new_book = book_schema.load(book, session=db.session).data
        db.session.add(new_book)
        db.session.commit()
        return book_schema.dump(new_book).data
    except ValidationError:
        return None


def update(book_id, book):
    """
    URL: /api/books/{book_id}
    :return: a updated book (if found)
    """
    try:
        found_book = Book.query.get(book_id)

        if found_book is not None:
            query_book = Book.query.filter_by(id=book_id)
            book_schema = BookSchema()
            query_book.update(book)
            db.session.commit()

            return book_schema.dump(found_book).data
    except ValidationError:
        return None


def delete(book_id):
    """
    URL: /api/books/{book_id}
    :return: None
    """
    try:
        book = Book.query.get(book_id)

        if book is not None:
            db.session.delete(book)
            db.session.commit()

            return None
    except ValidationError:
        return None
