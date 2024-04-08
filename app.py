import logging
from flask import Flask, request, jsonify
from supabase import create_client, Client

url: str = "https://cmiepeympwalidbddslj.supabase.co"  # Replace with your Supabase project URL
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtaWVwZXltcHdhbGlkYmRkc2xqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTIyNTEyNDgsImV4cCI6MjAyNzgyNzI0OH0.guO9E4oxXyzSPYtH14xmQYLkxbqfB-4l9oFcJwX4iUQ"  # Replace with your Supabase service role key
supabase: Client = create_client(url, key)

app = Flask(__name__)

@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json
    chat_id = data.get('chat_id')

    # Attempt to retrieve existing record for the chat_id
    response = supabase.table("user_messages").select("*").eq("chat_id", chat_id).single().execute()
    existing_data = response.data

    if existing_data:
        # User exists, update their record
        new_user_messages = existing_data["user_messages"] + [data.get("user_message")]
        new_bot_responses = existing_data["bot_responses"] + [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None]
        
        response = supabase.table("user_messages").update({
            "user_messages": new_user_messages,
            "bot_responses": new_bot_responses
        }).eq("chat_id", chat_id).execute()
    else:
        # New user, insert their first message
        response = supabase.table("user_messages").insert({
            "chat_id": chat_id,
            "user_messages": [data.get("user_message")],
            "bot_responses": [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None],
            "user_status": "new"
        }).execute()

    error = response.error
    if error:
        error_details = error.get('message', 'Unknown error') if error else 'No error message'
        app.logger.error(f"Failed to store data in Supabase: {error_details}")
        return jsonify({"success": False, "msg": f"Failed to store data in Supabase: {error_details}"}), 500

    app.logger.info("Data stored in Supabase successfully")
    return jsonify({"success": True, "msg": "Data stored in Supabase"}), 200






