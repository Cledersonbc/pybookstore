#!/usr/bin/env python3
from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('config/swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
