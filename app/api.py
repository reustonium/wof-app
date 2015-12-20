from flask import Flask
from flask_restful import Resource, Api
import os
import re

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
api = Api(app)


class Words(Resource):
    def get(self, expression):
        with open(os.path.join(APP_ROOT, 'american-english')) as f:
            words = f.read()
        exp = re.compile(str.replace(str(expression), '*', '?'))
        matches = exp.findall(words)
        return {'hello': matches}

api.add_resource(Words, '/api/v1/words/<string:expression>')

if __name__ == '__main__':
    app.run(debug=True)