import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Deck:
	
	def __init__(self):
		createdeck()
	
	def createdeck(self):
		self.cards = []
		for rank in ranks:
			for suit in suits:
				cards = cards + [(suit, rank)];

	def shuffle(self):
		random.shuffle(self.cards);

	def draw(self):
		return cards.pop();

	def __str__(self):
		print(cards)
