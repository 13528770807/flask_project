from flask import Flask, request

app = Flask(__name__)


@app.route('/photo', methods=['GET', 'POST'])
def photo():
    res = request.files.get('mypic')
    res.save('./static/apple.jpg')
    print('---------')
    return 'index'


@app.route('/')
def index():
    return 'hello'


if __name__ == "__main__":
    app.run()
