from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json
    print("Received data:", data)
    return jsonify({"success": True, "msg": "Data received"}), 200

    app.run()
