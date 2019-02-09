from flask import render_template
from flask import request
from wtforms.ext.sqlalchemy.orm import model_form

from pybookstore import app
from pybookstore import db
from pybookstore.models import Book


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/books/new', methods=['GET', 'POST'])
def newbook():

    if request.method == 'POST':
        book = Book()
        BookForm = model_form(Book)
        form = BookForm(request.form, obj=book)

        if form.validate():
            form.populate_obj(book)
            db.session.add(book)
            db.session.commit()

    return render_template('newbook.html')


@app.route('/books/view/<int:book_id>', methods=['GET'])
def viewbook(book_id):
    book = Book.query.get(book_id)

    # TODO redirect to 404 page if not found
    if book is not None:
        return render_template('readbook.html', book=book)

    return render_template('home.html')
