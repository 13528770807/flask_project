#!/usr/bin/env python3
from flask import Flask, render_template, request, flash
from flask_script import Manager

app = Flask(__name__)
app.secret_key = 'fsfdsfewqfewf'
manager = Manager(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([name, password, password2]):
                flash('参数不足')

        if password != password2:
            flash('用户名或密码不正确')

    if request.method == 'POST':
        print("none")

    return render_template('temp_01_a.html')


@app.route('/user')
def user():
    return "this is user"


# 中文是这样的
if __name__ == "__main__":
    manager.run()


