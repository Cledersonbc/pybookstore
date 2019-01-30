#!/usr/bin/env python3
from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='config/api')
app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/books/new')
def newbook():
    return render_template('newbook.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
