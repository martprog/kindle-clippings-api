from flask import request, jsonify, Blueprint
from parse import read_json_file

data_bp= Blueprint("data_bp", __name__)

@data_bp.route('/all', methods=['GET'])
def get_all_clipings():
    data = read_json_file()
    if data is None:
        return jsonify({'error': 'Oops... no data available. Check that your clippings exists and are in the right path'})
    else:
        return jsonify({"query": "All Records", "data":data})



@data_bp.route('/author', methods=['GET'])
def get_author():
    data = read_json_file()
    if data is None:
        return jsonify({'error': 'Oops... no data available. Check that your clippings exists and are in the right path'})
    query = request.args.get('name', None)

    if query is not None:
        matching_authors = [quote for quote in data if query.lower() in quote.get('author', '').lower()]
        if matching_authors:
            return jsonify({'query': query, 'quotes': matching_authors})
        else:
            return jsonify({'error': 'Author not found'}), 404
    else:
        return jsonify({'error': 'Author parameter missing'}), 400


@data_bp.route('/book/<int:quote_id>', methods=['GET'])
def get_book(quote_id):
    data = read_json_file()
    quote = next((q for q in data if q['quote_id'] == quote_id), None)
    if quote:
        book = quote.get('book', 'Unknown')
        return jsonify({'quote_id': quote_id, 'book': book})
    else:
        return jsonify({'error': 'Quote not found'}), 404