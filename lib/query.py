from flask import request, jsonify, Blueprint


def query_resource(data, query_key):
    query_param = request.args.get("name", None)

    if query_param is not None:
        matching_items = [item for item in data if query_param.lower() in item.get(query_key, '').lower()]
        if matching_items:
            return jsonify({'query': query_param, 'quotes': matching_items})
        else:
            return jsonify({'error': f'{query_key.capitalize()} not found'}), 404
    else:
        return jsonify({'error': f'{query_key.capitalize()} parameter missing'}), 400