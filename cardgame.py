# A Python Example
from random import shuffle, randint

class Card(object):

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

class Deck(object):

	def __init__(self):
		deckList = []
		for i in range(4): # traverse all suits
			for j in range(13): # traverse all values
				deckList.append(Card(i,j+1))
		shuffle(deckList)
		self.deck = deckList

class Player(object):

	def __init__(self, name):
		self.name = name
		self.cards = []

def printSuitAsString(suit):
	if suit == 0:
		return "H"
	elif suit == 1:
		return "C"
	elif suit == 2:
		return "D"
	elif suit == 3:
		return "S"

deck = Deck()
for card in deck.deck:
	print str(card.value) + "-" + printSuitAsString(card.suit)

print "-" * 20

player1 = Player("Stephen")
player2 = Player("Steward")

for i in range(5):
	player1.cards.append(deck.deck[i])
	player2.cards.append(deck.deck[i + 5])

stack1 = []
for card in player1.cards:
	stack1.append(str(card.value) + "-" + printSuitAsString(card.suit))

stack2 = []
for card in player2.cards:
	stack2.append(str(card.value) + "-" + printSuitAsString(card.suit))

print "-" * 20

