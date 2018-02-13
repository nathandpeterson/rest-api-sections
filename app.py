from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
    'name': 'My wonderful store',
    'items': {
        'name': 'Item',
        'price': 15.99
        }
    }
]

@app.route('/')
def home():
    return 'Hello World!'

# POST / store data: name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET / store / one
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return jsonify({'error': 'no such store'})

# GET / store / all
@app.route('/store')
def get_all_stores():
    return jsonify({'stores': stores})

# POST / add an item to a store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    for store in stores:
        if name == store['name']:
            store['items'].append(new_item)
            return jsonify(store['items'])
    return jsonify({'error': 'no such store'})

# GET / store / one / item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store['items'])
    return jsonify({'error': 'no such store'})


app.run(port=5000)
