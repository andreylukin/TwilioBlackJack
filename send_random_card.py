from __future__ import print_function # In python 2.7
import sys
from twilio.twiml.messaging_response import MessagingResponse, Message
from flask import Flask, request, redirect, session
from pprint import pprint
import requests
import requests.auth
import json


app = Flask(__name__)

def getRandomCard():
	r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1').json()
	deck_id = r['deck_id']
	card = requests.get("https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=1").json()
	cards = card['cards'][0]
	image = cards['image']
	return str(image)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(request.values.get('From'), file=sys.stderr)
    
    

    # Start our TwiML response
    resp = MessagingResponse()
    message = Message()
    # Determine the right reply for this message
    message.media(str(getRandomCard()))
    message.body("Heres your random card! Send another text to get a different one! ") 

    resp.append(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
