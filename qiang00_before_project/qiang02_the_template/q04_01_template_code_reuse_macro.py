from flask import Flask, render_template

app = Flask(__name__)


@app.route('/test_macro')
def test_macro():
    return render_template('test_macro.html')


@app.route('/macro')
def macro():
    return render_template('macro.html')


@app.route('/')
def index():
    return 'hello'


if __name__ == "__main__":
    app.run()