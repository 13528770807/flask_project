from flask import Flask
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        # print(url_map)
        # print(args)
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]

    def to_python(self, value):
        print('value:', value)
        print('user_id_str:', type(value))
        return int(value)


app = Flask(__name__)
app.url_map.converters['re'] = RegexConverter
# print(app)


@app.route('/demo1/<re("[0-9]{3}"):user_id>')
def demo1(user_id):
    print('user_id_int', type(user_id))
    return 'id: %s' % user_id


# @app.errorhandler(ValueError)
# def value_error(e):
#     return '不完整的格式'


if __name__ == "__main__":
    app.run(debug=True)