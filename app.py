# app.py
import subprocess
import uuid
from flask import Flask, request, jsonify, send_file
import requests
from werkzeug.utils import secure_filename
import os
import ffmpeg
from scipy.spatial import distance


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/postdata', methods=['POST'])
def postdata():
    # Get JSON data from the request
    data = request.json
    print("Received data:", data)
    # Respond with a success message
    return jsonify({"success": True, "msg": "Data received"}), 200

if __name__ == '__main__':
    app.run(debug=True)
