from flask import Flask
from flask_restful import Resource, Api

from search_api import Search
app = Flask(__name__)
api = Api(app)

api.add_resource(Search, '/search')

if __name__ == '__main__':
    app.run(debug=True)