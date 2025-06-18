import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()
# "SLACK_BOT_TOKEN" env key
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

# Fonction pour traiter les messages
def process_message(message):
    # Ici, vous intégreriez la logique de votre chatbot
    return "Vous avez dit : {message}"

# Écouter les messages dans les canaux où le bot est mentionné
@app.event("app_mention")
def handle_mention(event, say):
    message = event['text']
    response = process_message(message)
    say(response)

# Écouter les messages directs
@app.event("message")
def handle_message(event, say):
    if event.get('channel_type') == 'im':
        message = event['text']
        response = process_message(message)
        say(response)

# Démarrer votre app
# "SLACK_APP_TOKEN"
if __name__ == '__main__':
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()