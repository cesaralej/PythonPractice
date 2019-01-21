class Player:

    def __init__(self, balance, house=False):
        self.balance = balance
        self.hand = []
        self.value = 0
        self.aces = 0
        self.house = house

    def bet(self, minbet):
        while True:
            bet = input(f"\nYou curently have ${self.balance}. Please type the amount of money you want to bet. \n")
            try:
                if self.balance >= int(bet):
                    if int(bet) >= minbet:
                        self.balance = self.balance - int(bet)
                        print("\nBet Accepted!")
                        return int(bet)
                        break
                    else:
                        print(f"The minimum bet is {minbet}, please enter a higher amount of money!")
                else:
                    print("Funds Unavailable, please enter a lower amount of money!")
                    continue
            except ValueError:
                print("Only use numbers!")
                continue

    def resethand(self):
        self.hand = []
        self.aces = 0

    def calulatevalue(self):
        self.value = 0
        for card in self.hand:
            self.value = self.value + values[card[0]]
        if self.aces > 0:
            while self.value > 21:
                self.value -= 10
                self.aces -= 1

    def bust(self):
        return self.value > 21

    def draw(self, card):
        self.hand.append(card)
        if card[0] == "Ace":
            self.aces += 1

    def win(self, amount):
        self.balance = self.balance + amount
        print(f'!!!You won ${amount}!!! Your new balance is ${self.balance}.')

    def showhand(self):

        if self.house == False:
            print('\nYour current hand is: ')
            if len(self.hand) > 0:
                time.sleep(1)
                for card in self.hand:
                    print(f'--{card[0]} of {card[1]}')
                    time.sleep(1)
            else:
                print("There are no cards on your hand")

        else:
            print("\nThe House's hand is: ")
            time.sleep(1)
            for card in self.hand:
                print(f'--{card[0]} of {card[1]}')
                time.sleep(1)
