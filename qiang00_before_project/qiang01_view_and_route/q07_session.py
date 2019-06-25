from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'rewfdfsfef'


@app.route('/set_se')
def set_se():
    session['name'] = 'zhongruan'
    return redirect(url_for('index'))


@app.route('/')
def index():
    res = session.get('name')
    return res


if __name__ == "__main__":
    app.run()