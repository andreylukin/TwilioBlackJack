import os
from twilio.rest import Client


account_sid = "XXXXXXXX"
auth_token = "XXXXXXXXX"

aaki = "+XXXXXX"
justin = "+XXXXXX"
keshav = "+XXXXXXXX"
client = Client(account_sid, auth_token)

client.messages.create(
	to=justin,
	from_="+16467981327",
	body="This is Andrey trying to learn Twilio! Send a random string to get a card!",
)
