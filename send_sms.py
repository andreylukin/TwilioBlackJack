import os
from twilio.rest import Client


account_sid = "ACbe66967292816dd95aa89c4113e8a7d3"
auth_token = "20d83c1c9f1960831e026b8d351503fe"

client = Client(account_sid, auth_token)


client.messages.create(
	to="+15085966499",
	from_="+16467981327",
	body="Fuck you Justin"
)
