from flask import Flask, render_template, request, flash
from flask_script import Manager
from flask_wtf import Form
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.secret_key = 'adfsfeffwf'
manager = Manager(app)


class BaseFlaskForm(Form):
    username = StringField('用户名', validators=[DataRequired('验证：请输入用户名：')], render_kw={'placeholder': '我是占位符'})
    password = PasswordField('密码', validators=[DataRequired('请输入密码')])
    password2 = PasswordField('确认密码', validators=[DataRequired('请输入确认密码'), EqualTo('password', '两次密码输入不一致')])
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = BaseFlaskForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(username, password, password2)
        if login_form.validate_on_submit():
            print(username)
            return 'success'
        else:
            return '参数有误'

    return render_template('temp_02_flask_wtf.html',
                           form=login_form
                           )


if __name__ == '__main__':
    manager.run()