import logging
from flask import Flask, request, jsonify
from supabase import create_client, Client

url: str = "https://ednvihrgjszsftdhvteq.supabase.co"  # Replace with your Supabase project URL
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVkbnZpaHJnanN6c2Z0ZGh2dGVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE3NTU1NjUsImV4cCI6MjAyNzMzMTU2NX0.AnJ9EYgjCN_HshjM1eD21U1sHKxpCMBb6sAOcTeeIqs"  # Replace with your Supabase service role key
supabase: Client = create_client(url, key)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json
    chat_id = data.get('chat_id')

    # Attempt to retrieve existing records for the chat_id
    response, error = supabase.table("user_messages").select("*").eq("chat_id", chat_id).execute()

    if error:
        app.logger.error(f"Error retrieving data from Supabase: {error}")
        return jsonify({"success": False, "msg": "Error retrieving data from Supabase"}), 500

    existing_data = response.data
    if existing_data:
        # Existing records found, assume the first one (should be only one due to chat_id uniqueness)
        existing_record = existing_data[0]
        new_user_messages = existing_record["user_messages"] + [data.get("user_message")]
        new_bot_responses = existing_record["bot_responses"] + [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None]
        
        update_response, update_error = supabase.table("user_messages").update({
            "user_messages": new_user_messages,
            "bot_responses": new_bot_responses
        }).eq("chat_id", chat_id).execute()
    else:
        # No records found, this is a new user
        update_response, update_error = supabase.table("user_messages").insert({
            "chat_id": chat_id,
            "user_messages": [data.get("user_message")],
            "bot_responses": [data.get("bot_response")[0] if isinstance(data.get("bot_response"), list) else None],
            "user_status": "new"
        }).execute()

    if update_error:
        app.logger.error(f"Failed to store data in Supabase: {update_error.get('message', 'Unknown error')}")
        return jsonify({"success": False, "msg": f"Failed to store data in Supabase: {update_error.get('message', 'Unknown error')}"}), 500

    app.logger.info("Data stored in Supabase successfully")
    return jsonify({"success": True, "msg": "Data stored in Supabase"}), 200

if __name__ == "__main__":
    app.run(debug=True)






