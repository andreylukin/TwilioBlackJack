import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
	resp = MessagingResponse()
	resp.message("Lol, jk, this is Andrey fucking around with Twilio")
	
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)