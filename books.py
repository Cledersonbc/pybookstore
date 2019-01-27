#!/usr/bin/env python3


def read_example():
    import json
    try:
        with open('example/books.json') as json_data:
            return json.load(json_data)
    except FileNotFoundError as e:
        print('%s: %s'.format(e.strerror, e.filename))
        return None


def read():
    """
    This function responds requests to a response
    for /api/books
    """
    return read_example()
