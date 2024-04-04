import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def homepage():
    return "Homepage"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"


@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json
    print("Received data:", data)
    app.logger.info(f'Received data: {data}')  # Log the received data
    return jsonify({"success by Trixode-Studios": True, "msg": "Data received"}), 200




