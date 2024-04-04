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
    app.logger.info(f'Received data: {data}')
    
    # Attempt to insert the data into Supabase
    data_response= supabase.table("messages").insert({
        "chat_id": data.get('chat_id'),
        "user_message": data.get('user_message'),
        "bot_response": data['bot_response'][0] if data.get('bot_response') else None,
    }).execute()

    # Check if there was an error
    if error:
        app.logger.error(f"Failed to store data in Supabase. Error: {error}")
        return jsonify({"success": False, "msg": "Failed to store data in Supabase"}), 500



