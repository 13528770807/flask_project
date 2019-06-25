from flask import Flask, render_template, session, g, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'dfsdfsae'


@app.route('/set_session_url')
def set_session():
    session['company'] = 'zhongruan',
    print('------1---------')
    return redirect(url_for('index'))


@app.route('/user/<int:user_id>')
def user(user_id):
    return 'user_id: %s ' % user_id


@app.route('/')
def index():
    g.name = 'zhangsan'
    flash('hahahahahaha')
    return render_template('variable.html')


if __name__ == "__main__":
    app.run(debug=True)
