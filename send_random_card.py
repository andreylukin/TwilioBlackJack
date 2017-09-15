from __future__ import print_function # In python 2.7
import sys
from twilio.twiml.messaging_response import MessagingResponse, Message
from flask import Flask, request, redirect, session
from pprint import pprint
import requests
import requests.auth
import json
import psycopg2


app = Flask(__name__)

def connectToDB( query ):
	try:
		connect_str = "dbname='jack' user='jack' host='localhost' " + \
			  "password='password'"
		# use our connection values to establish a connection
		conn = psycopg2.connect(connect_str)
		conn.autocommit = True
		# create a psycopg2 cursor that can execute queries
		cursor = conn.cursor()	
		cursor.execute(str( query ))
		return cursor.fetchall() 
	except Exception as e:
		print("Uh oh, can't connect. Invalid dbname, user or password? I am " + query[:3])
		print(e)

def getDeck():
	r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1').json()
	deck_id = r['deck_id']
	return deck_id


def getRandomCard(deck_id):
	url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=1"
	print(url)
	cardsjson = requests.get(url).json()
	cards = cardsjson['cards'][0]
	image = cards['image']
	remaining = cardsjson['remaining']
	return {'image_url': str(image), 'remaining': remaining} 


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
	"""Send a dynamic reply to an incoming text message"""
	# Get the message the user sent our Twilio number
	from_ = str(request.values.get('From', None))[1:]
 	body = str(request.values.get('Body', None))	
	if len(connectToDB("SELECT * FROM tb_entity WHERE phone ilike '" + from_  + "';")) == 0:
		connectToDB("INSERT INTO tb_entity VALUES( default, '" + from_ + "', 100, '" + str(getDeck()) + "', default );")

	




	#    print(request.values.get('From'), file=sys.stderr)
	#    
	#    
	#
	# Start our TwiML response
	resp = MessagingResponse()
	message = Message()
	# Determine the right reply for this message
	deckOfCurrentUser = connectToDB("SELECT deck FROM tb_entity WHERE phone ilike '" + from_ + "';")[0][0]
	randomCard = getRandomCard(deckOfCurrentUser)
	message.media(randomCard['image_url'])
	message.media(randomCard['image_url'])
	message.body("Heres your random card! Send another text to get a different one! There are cards left" + str(randomCard['remaining'])) 

	resp.append(message)
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
