#!/usr/bin/evn python3
import base64
import os

from flask import Flask, render_template, request, flash, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'fewfsafdfsdaf'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)

        if not all([username, password]):
            flash('参数不足')
            print('参数不足')

        if username == 'zhangqiang' and password == '123456':
            response = redirect(url_for('transfer'))
            response.set_cookie('username', username)
            return response
    return render_template('temp_03_csrf_weba.html')


@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    csrf_token = generate_csrf()
    if request.method == 'POST':
        to_account = request.form.get('to_account')
        money = request.form.get('money')
        form_csrf_token = request.form.get('form_csrf_token')
        cookie_csrf_token = request.cookies.get('cookie_csrf_token')

        if form_csrf_token != cookie_csrf_token:
            return "非法请求"

        return '转账%s到%s成功' % (money, to_account)
    response = make_response(render_template('temp_03_csrf_transfer.html', csrf_token=csrf_token))
    response.set_cookie('cookie_csrf_token', csrf_token)
    return response


def generate_csrf():
    return bytes.decode(base64.b64encode(os.urandom(48)))


if __name__ == '__main__':
    app.run(port=9000, debug=True)