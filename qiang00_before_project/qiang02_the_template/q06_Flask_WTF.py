from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'afsdfdsfsds'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([username, password, password2]):
            flash('参数不足')

        elif password != password2:
            flash('密码不一致')

        else:
            print(username, password, password2)
            return 'success'

    return render_template('flask_wtf.html')


if __name__ == "__main__":
    app.run(debug=True)


