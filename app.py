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

    # Attempt to retrieve existing record for the chat_id
    response = supabase.table("user_messages").select("*").eq("chat_id", chat_id).execute()

    # Check for errors in the response
    if response.error:
        app.logger.error(f"Error retrieving data from Supabase: {response.error}")
        return jsonify({"success": False, "msg": "Error retrieving data from Supabase"}), 500

    existing_data = response.data
    if existing_data:
        # Existing record found
        app.logger.info("Existing record found")
        # Proceed with updating the existing record
    else:
        # No existing record found
        app.logger.info("No existing record found")
        # Proceed with inserting a new record

    return jsonify({"success": True, "msg": "Operation successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)







