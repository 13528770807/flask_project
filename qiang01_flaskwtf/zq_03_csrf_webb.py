#!/usr/bin/env python3
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return render_template('temp_03_csrf_webb.html')


if __name__ == '__main__':
    manager.run()