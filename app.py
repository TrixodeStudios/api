import logging
from flask import Flask, request, jsonify
from supabase import create_client, Client

url: str = "https://ednvihrgjszsftdhvteq.supabase.co"  # Replace with your Supabase project URL
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVkbnZpaHJnanN6c2Z0ZGh2dGVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE3NTU1NjUsImV4cCI6MjAyNzMzMTU2NX0.AnJ9EYgjCN_HshjM1eD21U1sHKxpCMBb6sAOcTeeIqs"  # Replace with your Supabase service role key
supabase: Client = create_client(url, key)

@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json
    chat_id = data.get('chat_id')

    # Attempt to retrieve existing record for the chat_id
    response, error = supabase.table("user_messages").select("*").eq("chat_id", chat_id).execute()

    # Check if there was an error with the request
    if error:
        app.logger.error(f"Supabase error: {error.message}")
        return jsonify({"success": False, "msg": "Error retrieving data from Supabase"}), 500

    existing_data = response.data if response else None

    if existing_data:
        # Existing record found, proceed with updating the record
        app.logger.info("Existing record found")
    else:
        # No existing record found, proceed with inserting a new record
        app.logger.info("No existing record found")

    # Proceed with your logic for updating or inserting data as needed...
    return jsonify({"success": True, "msg": "Operation successful"}), 200
    
    if __name__ == '__main__':
    app.run(debug=True)



