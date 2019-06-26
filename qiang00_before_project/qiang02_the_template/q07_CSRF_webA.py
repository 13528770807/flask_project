import base64
import os

from flask import Flask, render_template, request, flash, redirect, url_for, make_response

app = Flask(__name__)


def generate_csrf():
    res = bytes.decode(base64.b64encode(os.urandom(48)))
    return res


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not all([username, password]):
            flash('参数不足')

        else:
            if username == 'zhangsan' and password == '123456':
                resp = redirect(url_for('transfer'))
                resp.set_cookie('username', username)
                return resp
            else:
                flash('密码错误')
    return render_template('webA.html')


@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    csrf_token = generate_csrf()
    print('0==>', csrf_token)
    cookie = request.cookies.get('username', None)
    if not cookie:
        return redirect(url_for('index'))

    if request.method == 'POST':
        to_account = request.form.get('to_account')
        money = request.form.get('money')
        csrf_token_web = request.cookies.get('csrf_token')
        print('1==>', csrf_token_web)
        csrf_token_table = request.form.get('csrf_token')
        print('2==>', csrf_token_table)
        if csrf_token_web != csrf_token_table:
            return '非法操作'
        print('假装转帐')
        return '转帐: %s, 金额: %s 成功' % (to_account, money)

    response = make_response(render_template('transfer.html', csrf_token=csrf_token))
    response.set_cookie('csrf_token', csrf_token)
    return response


if __name__ == "__main__":
    app.run(debug=True)
