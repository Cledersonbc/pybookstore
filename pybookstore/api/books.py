import json
import os
from pybookstore import basedir


def read_example():
    try:
        path = os.path.join(basedir, 'example', 'books.json')
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
    print('aee')
    return read_example()


def read(bookId):
    """
    URL: /api/books/{bookId}
    :return: a book (if found) by ID
    """
    return None
