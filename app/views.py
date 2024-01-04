from flask import request, jsonify, Blueprint, current_app
from parse import read_json_file
from lib.query import query_resource

data_bp= Blueprint("data_bp", __name__)

#Loads json data before each request
@data_bp.before_request
def load_data():
    try:
        #assigns data to application context
        current_app.data = read_json_file()
    except FileNotFoundError:
        current_app.data = None

#All clippings
@data_bp.route('/all', methods=['GET'])
def get_all_clipings():
    if current_app.data is None:
        return jsonify({'error': 'Oops... no data available. Check that your clippings exists and are in the right path'})
    else:
        return jsonify({"query": "All Records", "data":current_app.data})

#Query by author name: author?name=
@data_bp.route('/author', methods=['GET'])
def get_author():
    if current_app.data is None:
        return jsonify({'error': 'Oops... no data available. Check that your clippings exists and are in the right path'})
    return query_resource(current_app.data, 'author')

#Query by author name: book?name=
@data_bp.route('/book', methods=['GET'])
def get_book():
    if current_app.data is None:
        return jsonify({'error': 'Oops... no data available. Check that your clippings exists and are in the right path'})
    return query_resource(current_app.data, 'title')
