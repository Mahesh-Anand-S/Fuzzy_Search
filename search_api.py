import re
from flask import jsonify
from flask_restful import Resource, reqparse
from common import load_words_file

words = load_words_file()


class Search(Resource):
    def get(self):
        req_parser = reqparse.RequestParser()
        req_parser.add_argument("word", type=str, location="args", required=True, help="")
        args = req_parser.parse_args()
        search_str = args['word']
        search_results = []
        temp_results = []
        for word in words:
            if type(word) != str:
                continue
            if re.search(search_str, word):
                temp_results.append(word)
        search_results_a = temp_results.copy()
        if search_str in temp_results:
            search_results.append(temp_results.pop(temp_results.index(search_str)))
            search_results_a.remove(search_str)
        for result in temp_results:
            if re.search('^' + search_str, result):
                search_results.append(result)
                search_results_a.remove(result)
        search_results.extend(search_results_a)
        return jsonify({'result': search_results[:25]})

