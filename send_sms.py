import os
from twilio.rest import Client


account_sid = "ACbe66967292816dd95aa89c4113e8a7d3"
auth_token = "20d83c1c9f1960831e026b8d351503fe"

aaki = "+17702625690"
justin = "+15085966499"
keshav = "+16319213220"
client = Client(account_sid, auth_token)

client.messages.create(
	to=justin,
	from_="+16467981327",
	body="This is Andrey trying to learn Twilio! Send a random string to get a card!",
)
