from flask import Flask, request, flash, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'SECRET_KEY'


class RegistForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired('请输入用户名:')], render_kw={'placeholder': '占位符'})
    password = PasswordField('密码', validators=[DataRequired('请输入密码')])
    password2 = PasswordField('确认密码', validators=[DataRequired('确认密码'), EqualTo("password", "两次密码不一致")])
    submit = SubmitField('提交')


@app.route('/flaskwtf', methods=['GET', 'POST'])
def flaskwtf():
    regist = RegistForm()
    if regist.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(username, password, password2)
        return 'success'

    else:
        if request.method == 'POST':
            flash('参数不完整')

    return render_template('flask_wtf2.html', form=regist)


if __name__ == '__main__':
    app.run(debug=True)
