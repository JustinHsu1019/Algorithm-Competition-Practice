from flask import Flask, request, jsonify
from flask_limiter import Limiter, util

app = Flask(__name__)

limiter = Limiter(
    app=app,
    key_func=util.get_remote_address
)

tree = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 5],
    4: [1, 6],
    5: [2, 3, 7, 8],
    6: [4, 7],
    7: [5, 6],
    8: [5]
}

@app.route('/')
def hello_world_main():
    return 'Hello World!!!'

@app.route('/TreeNode/')
def hello_world():
    return 'Service is ready!!!'

@app.route('/TreeNode/get_neighbours', methods=['GET'])
@limiter.limit("5 per minute")
def get_neighbours_api():
    key = request.args.get('key')

    if not key:
        return jsonify({"error": "No key provided."}), 400

    try:
        key = int(key)
        if key in tree:
            return jsonify({"neighbours": tree[key]})
        else:
            return jsonify({"error": "Key not found in the tree."}), 404
    except ValueError:
        return jsonify({"error": "Invalid key provided."}), 400

if __name__ == '__main__':
    app.run()
