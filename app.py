import logging
from flask import Flask, request, jsonify
from supabase import create_client, Client

url: str = "https://cmiepeympwalidbddslj.supabase.co"  # Replace with your Supabase project URL
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtaWVwZXltcHdhbGlkYmRkc2xqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTIyNTEyNDgsImV4cCI6MjAyNzgyNzI0OH0.guO9E4oxXyzSPYtH14xmQYLkxbqfB-4l9oFcJwX4iUQ"  # Replace with your Supabase service role key
supabase: Client = create_client(url, key)


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# @app.route('/postdata', methods=['POST'])
# def postdata():
#     data = request.json
#     print("Received data:", data)
#     app.logger.info(f'Received data: {data}')  # Log the received data
#     return jsonify({"success by Trixode-Studios": True, "msg": "Data received"}), 200


@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json
    print("Received data:", data)
    app.logger.info(f'Received data: {data}')  # Log the received data
    # Extract relevant information
    chat_id = data.get('chat_id')
    message = data.get('message')
    sender_id = data.get('sender_id')

    # Insert the data into the Supabase "messages" table
    response = supabase.table("messages").insert({
        "chat_id": chat_id,
        "message": message,
        "sender_id": sender_id
    }).execute()

    # Check if insertion was successful
    if response.status_code in range(200, 300):
        return jsonify({"Success by Trixode-Studios": True, "msg": "Data received & Message stored in Supabase Infinitys data base."}), 200
    else:
        return jsonify({"success": False, "msg": "Failed to store message"}), response.status_code




