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
    
    bot_response_text = data['bot_response'][0] if data.get('bot_response') else None
    
    # Prepare the data for insertion
    insert_data = {
        "chat_id": data.get('chat_id'),
        "user_message": data.get('user_message'),
        "bot_response": bot_response_text,
    }
    
    # Insert the data into the Supabase "messages" table
    response = supabase.table("messages").insert(insert_data).execute()
    
    # Check if the operation was successful
    if response.error is None:
        print("Data stored in Supabase successfully")
        return jsonify({"success": True, "msg": "Data stored in Supabase"}), 200
    else:
        print(f"Failed to store data in Supabase: {response.error}")
        return jsonify({"success": False, "msg": f"Failed to store data in Supabase: {response.error.message}"}), 400






