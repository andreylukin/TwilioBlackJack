from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()
    message = Message()	
    # Determine the right reply for this message
    if body == 'hello':
        message.body("Hi!")
	message.media("https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg")
    elif body == 'bye':
        message.body("Goodbye")

    resp.append(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
