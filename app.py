from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

drinks = [

    {
        'name': 'cola',
        'description': 'Cola is a carbonated soft drink flavored with vanilla,',


        'items': [{
            'type': 'cool',
            'price': 10
        }]
    }
]


@app.route("/drink", methods=['POST'])
def create_store():
    request_data = request.get_json()
    now_drink = {
        "name"        :request_data['name'],
        "description" :['description'],
    }
    drinks.append(now_drink)
    return jsonify(now_drink)


@app.route("/drink/<string:name>", methods=['GET'])
def get_drink(name):
    for drink in drinks:
        if drink['name'] == name:
            return jsonify(drink)
    return jsonify({'message': 'Drink not found'})



@app.route('/drink/<string:name>/item', methods=['POST'])
def create_item_in_drink(name):
    request_data = request.get_json()
    for drink in drinks:
        if drink['name'] == name:
            now_item = {
                'type' : request_data['type'],
                'price': request_data['price']
            }
            drink['items'].append(now_item)
            return jsonify(now_item)
    return jsonify({'message': name + ' store not found'})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
