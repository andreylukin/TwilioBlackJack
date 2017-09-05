from pprint import pprint 
import requests
import requests.auth
import json

def getRandomCard():
	r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1').json()

	deck_id = r['deck_id']
	print(deck_id)


	card = requests.get("https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=1").json()
	cards = card['cards'][0]
	image = cards['image']
	return str(image)
print(getRandomCard())

