from flask import Flask, request, jsonify, redirect, url_for

# 配置对象
# class Config(object):
#     DEBUG = True


app = Flask(__name__)
# app.config.from_object(Config)  # 对象
# app.config.from_pyfile('config.ini')  # 配置文件
# app.config.from_envvar('CONFIGABC')  # 环境变量


@app.route('/demo1')
def demo1():
    return "demo1"


@app.route('/demo2/<user_id>')
def demo2(user_id):
    return 'demo2 %s' % user_id


@app.route('/demo3/<int:user_id2>', methods=['GET', 'POST'])
def demo3(user_id2):
    return 'demo3 %d %s' % (user_id2, request.method)


@app.route('/demo4')
def demor():
    json = {
        'name': 'zhangsan',
        'age': 30
    }
    return jsonify(json)


@app.route('/demo5')
def demo5():
    return redirect('https://www.baidu.com')


@app.route('/demo6')
def demo6():
    return redirect(url_for('demo3', user_id2=999))


@app.route('/demo7')
def demo7():
    return 'code 666', 666


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)