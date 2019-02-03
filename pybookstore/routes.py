from flask import render_template
from pybookstore import app, api


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/books/new', methods=['GET', 'POST'])
def newbook():
    return render_template('newbook.html')


@app.route('/books/view/<int:book_id>')
def viewbook(book_id):
    context = api.books.read_example()

    return render_template('readbook.html', context=context)
