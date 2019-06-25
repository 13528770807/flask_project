from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def set_cookie():
    res = make_response('this is the set cookie')
    res.set_cookie('username', 'zhangsan')  # 设置cookie
    return res


@app.route('/response')
def resp_cookie():
    res = request.cookies.get('username')  # 拿到客戶端带过来的cookie, 并返回
    return res


if __name__ == "__main__":
    app.run(debug=True)