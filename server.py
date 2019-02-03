#!/usr/bin/env python3
from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='config/api')
app.add_api('swagger.yml')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/books/new', methods=['GET', 'POST'])
def newbook():
    return render_template('newbook.html')


@app.route('/books/view/<int:book_id>')
def viewbook(book_id):
    import api
    context = api.books.read_example()

    return render_template('readbook.html', context=context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
