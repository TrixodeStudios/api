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
# @app.route('/postdata', methods=['POST'])
# def postdata():
#     data = request.json
#     app.logger.info(f"Received data: {data}")

#     bot_response_text = data['bot_response'][0] if data.get('bot_response') else None

#     # Perform the insert operation
#     response_data, error = supabase.table("messages").insert({
#         "chat_id": data.get('chat_id'),
#         "user_message": data.get('user_message'),
#         "bot_response": bot_response_text,
#     }).execute()

#     # Check if there was an error
#     if error:
#         app.logger.error(f"Failed to store data in Supabase: {error}")
#         return jsonify({"success": False, "msg": "Failed to store data in Supabase"}), 500

#     # If no error, proceed as successful
#     return jsonify({"success": True, "msg": "Data stored in Supabase"}), 200
# @app.route('/postdata', methods=['POST'])
# def postdata():
#     data = request.json
#     # Process the incoming data...
    
#     # Example insert operation
#     response_data, error = supabase.table("messages").insert({
#         "chat_id": data.get('chat_id'),
#         "user_message": data.get('user_message'),
#         "bot_response": data.get('bot_response'),
#     }).execute()
    
#     # Error handling
#     if error:
#         # Adapt error logging based on the type of the error object
#         error_description = f"Failed to store data in Supabase: {error}"
#         if hasattr(error, 'message'):
#             error_description = f"Failed to store data in Supabase: {error.message}"
#         elif isinstance(error, tuple):
#             error_description = f"Failed to store data in Supabase: {error[0]} with details {error[1]}"
        
#         app.logger.error(error_description)
#         return jsonify({"success": False, "msg": "Failed to store data in Supabase"}), 500
    
#     # If no error, assume success
#     return jsonify({"success": True, "msg": "Data stored in Supabase"}), 200
@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json

    # Perform the insert operation
    response_data, error = supabase.table("messages").insert({
        "chat_id": data.get('chat_id'),
        "user_message": data.get('user_message'),
        "bot_response": data.get('bot_response')[0] if isinstance(data.get('bot_response'), list) else None,
    }).execute()

    # Check for actual error
    if error:
        # Improved error handling logic
        error_description = "Failed to store data in Supabase"
        if hasattr(error, 'message'):
            error_description += f": {error.message}"
        elif isinstance(error, tuple):
            error_description += f": {error[0]} with details {error[1]}"
        else:
            error_description += f": Unknown error format {error}"
        
        app.logger.error(error_description)
        return jsonify({"success": False, "msg": error_description}), 500
    
    # If the insertion was successful
    app.logger.info("Data stored in Supabase successfully")
    return jsonify({"success": True, "msg": "Data stored in Supabase"}), 200




