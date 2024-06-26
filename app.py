#-----------------FIRST VERSION OF API FOR INFINITYS----------------------------

# import logging
# from flask import Flask, request, jsonify
# from supabase import create_client, Client

# url: str = "https://ednvihrgjszsftdhvteq.supabase.co"  # Replace with your Supabase project URL
# key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVkbnZpaHJnanN6c2Z0ZGh2dGVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE3NTU1NjUsImV4cCI6MjAyNzMzMTU2NX0.AnJ9EYgjCN_HshjM1eD21U1sHKxpCMBb6sAOcTeeIqs"  # Replace with your Supabase service role key
# supabase: Client = create_client(url, key)

# # Flask app setup
# app = Flask(__name__)
# logging.basicConfig(level=logging.INFO)

# @app.route('/postdata', methods=['POST'])
# def postdata():
#     data = request.json
#     chat_id = data.get('chat_id')

#     # Attempt to retrieve existing record for the chat_id
#     response = supabase.table("user_messages").select("*").eq("chat_id", chat_id).execute()
#     existing_data = response.data

#     # Check for existing data and append new messages accordingly
#     if existing_data and len(existing_data) > 0:
#         existing_record = existing_data[0]
#         new_user_messages = existing_record["user_messages"] + [data.get("user_message")]
#         new_bot_responses = existing_record["bot_responses"] + [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None]

#         update_response = supabase.table("user_messages").update({
#             "user_messages": new_user_messages,
#             "bot_responses": new_bot_responses
#         }).eq("chat_id", chat_id).execute()

#     else:
#         # New chat, insert the first set of messages
#         insert_response = supabase.table("user_messages").insert({
#             "chat_id": chat_id,
#             "user_messages": [data.get("user_message")],
#             "bot_responses": [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None],
#             "user_status": "new"
#         }).execute()

#     # Check for and handle errors
#     error = response.error if 'error' in response else None
#     if error:
#         error_details = error.get('message', 'Unknown error') if error else 'No error message available'
#         app.logger.error(f"Failed to store data in Supabase: {error_details}")
#         return jsonify({"success": False, "msg": f"Failed to store data in Supabase: {error_details}"}), 500

#     # Success response
#     app.logger.info("Data stored in Supabase successfully by Trixode-Studios")
#     return jsonify({"success": True, "msg": "Data stored in Supabase successfully"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)


#-----------------SECOND VERSION OF API FOR INFINITYS----------------------------

# import logging
# from flask import Flask, request, jsonify
# from supabase import create_client, Client

# url: str = "https://ednvihrgjszsftdhvteq.supabase.co"  # Replace with your Supabase project URL
# key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVkbnZpaHJnanN6c2Z0ZGh2dGVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE3NTU1NjUsImV4cCI6MjAyNzMzMTU2NX0.AnJ9EYgjCN_HshjM1eD21U1sHKxpCMBb6sAOcTeeIqs"  # Replace with your Supabase service role key
# supabase: Client = create_client(url, key)

# # Flask app setup
# app = Flask(__name__)
# logging.basicConfig(level=logging.INFO)

# @app.route('/postdata', methods=['POST'])
# def postdata():
#     data = request.json
#     chat_id = data.get('chat_id')

#     # Attempt to retrieve existing record for the chat_id
#     response = supabase.table("user_messages").select("*").eq("chat_id", chat_id).execute()
#     existing_data = response.data

#     # Check for existing data and append new messages accordingly
#     if existing_data and len(existing_data) > 0:
#         existing_record = existing_data[0]
#         new_user_messages = existing_record["user_messages"] + [data.get("user_message")]
#         new_bot_responses = existing_record["bot_responses"] + [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None]

#         update_response = supabase.table("user_messages").update({
#             "user_messages": new_user_messages,
#             "bot_responses": new_bot_responses
#         }).eq("chat_id", chat_id).execute()

#     else:
#         # New chat, insert the first set of messages
#         insert_response = supabase.table("user_messages").insert({
#             "chat_id": chat_id,
#             "user_messages": [data.get("user_message")],
#             "bot_responses": [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None],
#         }).execute()

    
#     # Check for and handle errors
#     error = response.error if 'error' in response else None
#     if error:
#         error_details = error.get('message', 'Unknown error') if error else 'No error message available'
#         app.logger.error(f"Failed to store data in Supabase: {error_details}")
#         return jsonify({"success": False, "msg": f"Failed to store data in Supabase: {error_details}"}), 500

#     # Success response
#     app.logger.info("Data stored in Supabase successfully by Trixode-Studios")
#     return jsonify({"success": True, "msg": "Data stored in Supabase successfully"}), 200

# @app.route('/getdata', methods=['GET'])
# def getdata():
#     # Retrieve all records from the user_messages table
#     response = supabase.table("user_messages").select("*").execute()
#     data = response.data

#     # Check for and handle errors
#     error = response.error if 'error' in response else None
#     if error:
#         error_details = error.get('message', 'Unknown error') if error else 'No error message available'
#         app.logger.error(f"Failed to fetch data from Supabase: {error_details}")
#         return jsonify({"success": False, "msg": f"Failed to fetch data from Supabase: {error_details}"}), 500

#     # Success response
#     return jsonify({"success": True, "data": data}), 200
# if __name__ == '__main__':
#     app.run(debug=True)



#-----------------THIRD VERSION OF API FOR INFINITYS----------------------------



# import logging
# from flask import Flask, request, jsonify
# from supabase import create_client, Client

# url: str = "https://ednvihrgjszsftdhvteq.supabase.co"  # Replace with your Supabase project URL
# key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVkbnZpaHJnanN6c2Z0ZGh2dGVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE3NTU1NjUsImV4cCI6MjAyNzMzMTU2NX0.AnJ9EYgjCN_HshjM1eD21U1sHKxpCMBb6sAOcTeeIqs"  # Replace with your Supabase service role key
# supabase: Client = create_client(url, key)

# # Flask app setup
# app = Flask(__name__)
# logging.basicConfig(level=logging.INFO)

# @app.route('/postdata', methods=['POST'])
# def postdata():
#     data = request.json
#     chat_id = data.get('chat_id')
#     nickname = data.get('nickname')

#     # Attempt to retrieve existing record for the chat_id
#     response = supabase.table("user_messages").select("*").eq("chat_id", chat_id).execute()
#     existing_data = response.data

#     # Check for existing data and append new messages accordingly
#     if existing_data and len(existing_data) > 0:
#         existing_record = existing_data[0]
#         new_user_messages = existing_record["user_messages"] + [data.get("user_message")]
#         new_bot_responses = existing_record["bot_responses"] + [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None]

#         update_response = supabase.table("user_messages").update({
#             "user_messages": new_user_messages,
#             "bot_responses": new_bot_responses
#         }).eq("chat_id", chat_id).execute()

#     else:
#         # New chat, insert the first set of messages
#         insert_response = supabase.table("user_messages").insert({
#             "chat_id": chat_id,
#             "nickname": nickname,
#             "user_messages": [data.get("user_message")],
#             "bot_responses": [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None],
#         }).execute()

    
#     # Check for and handle errors
#     error = response.error if 'error' in response else None
#     if error:
#         error_details = error.get('message', 'Unknown error') if error else 'No error message available'
#         app.logger.error(f"Failed to store data in Supabase: {error_details}")
#         return jsonify({"success": False, "msg": f"Failed to store data in Supabase: {error_details}"}), 500

#     # Success response
#     app.logger.info("Data stored in Supabase successfully by Trixode-Studios")
#     return jsonify({"success": True, "msg": "Data stored in Supabase successfully"}), 200

# @app.route('/getdata', methods=['GET'])
# def getdata():
#     # Retrieve all records from the user_messages table
#     response = supabase.table("user_messages").select("*").execute()
#     data = response.data

#     # Check for and handle errors
#     error = response.error if 'error' in response else None
#     if error:
#         error_details = error.get('message', 'Unknown error') if error else 'No error message available'
#         app.logger.error(f"Failed to fetch data from Supabase: {error_details}")
#         return jsonify({"success": False, "msg": f"Failed to fetch data from Supabase: {error_details}"}), 500

#     # Success response
#     return jsonify({"success": True, "data": data}), 200

# if __name__ == '__main__':
#     app.run(debug=True)


#-----------------Fourth VERSION OF API FOR INFINITYS----------------------------
import logging
from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

# --- Configuration ---
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

if not all([SUPABASE_URL, SUPABASE_KEY]):
    raise ValueError("Missing required Supabase environment variables.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# --- Helper Function to Update or Insert Messages --- 
def update_or_insert_messages(data):
    chat_id = data.get('chat_id')
    nickname = data.get('nickname')
    user_message = data.get("messages").get("user") # Correctly access user message
    bot_response = data.get("messages").get("gemini") # Correctly access bot response

    # Ensure bot_response is a list
    if not isinstance(bot_response, list):
        bot_response = [bot_response]

    response = supabase.table("messages").select("*").eq("chat_id", chat_id).execute()
    existing_data = response.data

    if existing_data:
        existing_record = existing_data[0]
        supabase.table("messages").update({ 
            "user_messages": existing_record["user_messages"] + [user_message],
            "bot_responses": existing_record["bot_responses"] + bot_response
        }).eq("chat_id", chat_id).execute()
    else:
        supabase.table("messages").insert({ 
            "chat_id": chat_id,
            "nickname": nickname,
            "user_messages": [user_message],
            "bot_responses": bot_response,
        }).execute()

# --- API Endpoint ---
@app.route('/postdata', methods=['POST'])
def postdata():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"success": False, "msg": "No JSON data provided"}), 400 

        update_or_insert_messages(data)
        app.logger.info("Data stored in Supabase successfully by Trixode-Studios")
        return jsonify({"success": True, "msg": "Data stored in Supabase successfully"}), 200

    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

