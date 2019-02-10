from flask import flash
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from wtforms.ext.sqlalchemy.orm import model_form

from pybookstore import app
from pybookstore import db
from pybookstore.models import Book


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/books/new', methods=['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        book = Book()
        BookForm = model_form(Book)
        form = BookForm(request.form, obj=book)

        if form.validate():
            form.populate_obj(book)
            db.session.add(book)
            db.session.commit()

            book_info = book.title + ' - ' + book.author
            flash(f'The Book "{book_info}" was added successfully.', 'success')

            return redirect(url_for('index'))

    return render_template('newbook.html')


@app.route('/books/view/<int:book_id>', methods=['GET'])
def view_book(book_id):
    book = Book.query.get(book_id)

    # TODO redirect to 404 page if not found
    if book is not None:
        return render_template('readbook.html', book=book)

    return render_template('home.html')


@app.route('/books/mybooks', methods=['GET'])
def view_all_books():
    books = Book.query.all()

    if books is not None:
        return render_template('allbooks.html', books=books)


@app.route('/books/del', methods=['POST'])
def del_book():
    book_id = request.form['book_id']
    book = Book.query.get(book_id)

    if book is not None:
        book_info = book.title + ' - ' + book.author
        db.session.delete(book)
        db.session.commit()

        flash(f'Book "{book_info}" was removed successfully.', 'success')
        return redirect(url_for('index'))
    else:
        flash('Error! Book not found to be removed.', 'error')
        return redirect(url_for('index'))


@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get(book_id)

    if book is None:
        flash('Error! Book not found to be updated.', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        BookForm = model_form(Book)
        form = BookForm(request.form, obj=book)

        if form.validate():
            form.populate_obj(book)
            db.session.add(book)
            db.session.commit()

            book_info = book.title + ' - ' + book.author
            flash(f'The Book "{book_info}" was updated successfully.',
                  'success')
            print('updated')
            return redirect(url_for('index'))

    return render_template('editbook.html', book=book)
