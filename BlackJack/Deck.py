class Deck:

    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                self.cards = self.cards + [(rank, suit)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __str__(self):
        deckstring = "This is your deck:\n"

        for card in self.cards:
            deckstring = deckstring + f"{card[0]} of {card[1]} \n"

        return deckstring
