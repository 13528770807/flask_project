from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    comments = [1, 2, 3]
    my_list = [
        {
            'id': 1,
            'value': '我爱工作'
        },
        {
            'id': 2,
            'value': '工作使我快乐'
        },
        {
            'id': 3,
            'value': '我要环游世界'
        },
        {
            'id': 4,
            'value': '杭州天气不错'
        },
        {
            'id': 5,
            'value': '你准备好了吗'
        }
    ]
    return render_template('control.html', comm=comments, my_list=my_list)


if __name__ == "__main__":
    app.run()