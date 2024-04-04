import logging
from flask import Flask, request, jsonify
from supabase import create_client, Client

url: str = ""  # Replace with your Supabase project URL
key: str = ""  # Replace with your Supabase service role key
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
    app.logger.info("Received data: %s", data)

    # Prepare the data for insertion
    insert_data = {
        "chat_id": data.get('chat_id'),
        "user_message": data.get('user_message'),
        "bot_response": data['bot_response'][0] if data.get('bot_response') else None,
    }

    # Insert the data into the Supabase "messages" table
    response, error = supabase.table("messages").insert(insert_data).execute()

    # Check if the operation was successful
    if error is None:
        app.logger.info("Data stored in Supabase successfully")
        return jsonify({"success": True, "message": "Data stored in Supabase"}), 200
    else:
        app.logger.error("Failed to store data in Supabase: %s", error.message)
        return jsonify({"success": False, "message": "Failed to store data in Supabase", "error": error.message}), 400





