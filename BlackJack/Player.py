class Player:

    def __init__ (self, balance=5000):
        if name == "house":
            self.balance = 5000
            self.house = True
        else:
            self.balance = balance
        self.hand = []
        self.value = 0
        self.aces = 0
           
    def bet(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print ("Funds Unavailable")

    def draw(self):
        hand = hand + deck.draw()
        if ace in hand:
            self.aces =+ 1

    def turn(self):
        move = input('Hit or stand? ')
        if move.lowercase() == ('h' or 'hit'):
            hand = hand + deck.draw()

    def calulatevalue(self):
        if self.aces > 0:
            for card in hand:
                value = values[card]

    def bust(self):
        return sum(hand) > 21


    def printhand(self):
        print (hand)

    def win(self, amount):
        self.balance = self.balance + amount

    def showhand(self):
        if house:
            print(hand[1:])
        else:
            print(hand)

