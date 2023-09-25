from flask import Flask, render_template, request, jsonify
from chat import chatbot
import requests  # Import the requests library

app = Flask(__name__)

# LanguageTool API URL
LANGUAGE_TOOL_URL = 'https://languagetool.org/api/v2/check'

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])

    # Define the parameters for the LanguageTool API request
    params = {
        'text': message,
        'language': 'en-US',  # Specify the language
    }

    # Send a POST request to the LanguageTool API
    response = requests.post(LANGUAGE_TOOL_URL, data=params)

    # Check if the request was successful and parse the JSON response
    if response.status_code == 200:
        data = response.json()
        if 'matches' in data:
            # Extract the first suggestion as the corrected text
            corrections = [match['replacements'][0]['value'] for match in data['matches']]
            corrected_text = ' '.join(corrections)
        else:
            corrected_text = message
    else:
        # If there was an issue with the API request, use the original message
        corrected_text = message

    bot_response = chatbot(corrected_text)
    return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == "__main__":
    app.run()
