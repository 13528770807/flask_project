from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    li = [1, 2, 3, 4, 5, 6, 7]
    return render_template('filter.html', li=li)


@app.template_filter('li_rv2')  # 添加过滤器 方法二
def li_reverse(li):
    res = list(li)
    res.reverse()
    return res


# app.add_template_filter(li_reverse, 'li_rv')  # 添加过滤器 方法一


if __name__ == "__main__":
    app.run(debug=True)
