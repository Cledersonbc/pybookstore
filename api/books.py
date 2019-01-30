#!/usr/bin/env python3


def read_example():
    import json
    try:
        with open('example/books.json') as json_data:
            return json.load(json_data)
    except FileNotFoundError as e:
        print('%s: %s'.format(e.strerror, e.filename))
        return None


def read_all():
    """
    URL: /api/books
    :return: a list of books
    """
    return read_example()


def read(bookId):
    """
    URL: /api/books/{bookId}
    :return: a book (if found) by ID
    """
    return None
