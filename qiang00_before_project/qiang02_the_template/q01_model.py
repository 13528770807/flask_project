from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    dic = {
        "name": "laowang",
        'age': 29,
        'li': [11, 22, 33, 44, 55, 66],
        'user': 'user_id'
    }
    return render_template('model.html', dic1=dic)


if __name__ == "__main__":
    app.run(debug=True)