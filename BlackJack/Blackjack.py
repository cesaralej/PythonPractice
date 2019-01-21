import random
import time
from Deck import Deck
from Player import Player


# suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True
initialbalance = 5000
minimumbet = 200
winmultiplier = 2


# class Deck:

#     def __init__(self):
#         self.cards = []
#         for rank in ranks:
#             for suit in suits:
#                 self.cards = self.cards + [(rank, suit)]

#     def shuffle(self):
#         random.shuffle(self.cards)

#     def deal(self):
#         return self.cards.pop()

#     def __str__(self):
#         deckstring = "This is your deck:\n"

#         for card in self.cards:
#             deckstring = deckstring + f"{card[0]} of {card[1]} \n"

#         return deckstring


# class Player:

#     def __init__(self, balance, house=False):
#         self.balance = balance
#         self.hand = []
#         self.value = 0
#         self.aces = 0
#         self.house = house

#     def bet(self, minbet):
#         while True:
#             bet = input(f"\nYou curently have ${self.balance}. Please type the amount of money you want to bet. \n")
#             try:
#                 if self.balance >= int(bet):
#                     if int(bet) >= minbet:
#                         self.balance = self.balance - int(bet)
#                         print("\nBet Accepted!")
#                         return int(bet)
#                         break
#                     else:
#                         print(f"The minimum bet is {minbet}, please enter a higher amount of money!")
#                 else:
#                     print("Funds Unavailable, please enter a lower amount of money!")
#                     continue
#             except ValueError:
#                 print("Only use numbers!")
#                 continue

#     def resethand(self):
#         self.hand = []
#         self.aces = 0

#     def calulatevalue(self):
#         self.value = 0
#         for card in self.hand:
#             self.value = self.value + values[card[0]]
#         if self.aces > 0:
#             while self.value > 21:
#                 self.value -= 10
#                 self.aces -= 1

#     def bust(self):
#         return self.value > 21

#     def draw(self, card):
#         self.hand.append(card)
#         if card[0] == "Ace":
#             self.aces += 1

#     def win(self, amount):
#         self.balance = self.balance + amount
#         print(f'!!!You won ${amount}!!! Your new balance is ${self.balance}.')

#     def showhand(self):

#         if self.house == False:
#             print('\nYour current hand is: ')
#             if len(self.hand) > 0:
#                 time.sleep(1)
#                 for card in self.hand:
#                     print(f'--{card[0]} of {card[1]}')
#                     time.sleep(1)
#             else:
#                 print("There are no cards on your hand")

#         else:
#             print("\nThe House's hand is: ")
#             time.sleep(1)
#             for card in self.hand:
#                 print(f'--{card[0]} of {card[1]}')
#                 time.sleep(1)

# Ask for replay


def replay():
    return input('\nDo you want to play again? (y/n) \n') == ('y')


# Blackjack loop
while playing:

    # Start Screen
    print('\n-----------------------------')
    print('----Welcome to Blackjack!----')
    print('-----------------------------')
    if input('\nWant to learn how to play? (y/n) \n') == 'y':
        print("\nYou'll start with $5000, Press s to stand or h to hit")

    input('\nPress Enter to start!')

    # Create Player
    player = Player(initialbalance)
    house = Player(initialbalance * 10, True)

    # Table Loop
    while True:

        # Single Game Loop
        while True:

            # Create a Deck and shuffle
            deck = Deck()
            deck.shuffle()

            # Reset Player Hand
            player.resethand()
            house.resethand()

            bust = False
            print('\n----------New Game!----------')

            # bet
            bet = player.bet(minimumbet)

            # initial house draw
            house.draw(deck.deal())
            house.draw(deck.deal())
            house.calulatevalue()
            house.showhand()

            # initial player draw
            player.draw(deck.deal())
            player.draw(deck.deal())
            player.calulatevalue()
            player.showhand()

            # Hit or Stand loop
            while True:

                # Ask for move
                move = input('\nHit or stand? (h/s) \n')

                # Hit
                if move.lower() == ('h'):
                    newcard = deck.deal()
                    player.draw(newcard)
                    player.calulatevalue()
                    time.sleep(1)
                    print('\nYour new card is...')
                    time.sleep(1)
                    print(f'--{newcard[0]} of {newcard[1]}')

                    # Check if bust
                    if player.bust():
                        time.sleep(1)
                        print('\n!!!Bust!!! ')
                        time.sleep(1)
                        bust = True
                        break

                    # No bust? then ask again
                    continue

                # Stand
                elif move.lower() == ('s'):
                    break

                # Incorrect input
                else:
                    print('Please insert a valid input.')
            # Hit or Stand loop end

            # The player did not bust, then the house plays
            if not bust:

                # house loop starts
                housebust = False
                while house.value <= 17:
                    newcard = deck.deal()
                    house.draw(newcard)
                    house.calulatevalue()
                    time.sleep(1)
                    print("\nThe House's new card is...")
                    time.sleep(1)
                    print(f'--{newcard[0]} of {newcard[1]}')

                    # Check if bust
                    if house.bust():
                        time.sleep(1)
                        print('\n!!!Bust for The House!!!')
                        time.sleep(1)
                        housebust = True
                        player.win(bet * winmultiplier)
                # house loop end

                # Check who won if no one busted
                if not housebust:
                    if house.value < player.value:
                        player.win(bet * winmultiplier)
                    elif house.value > player.value:
                        print('\nYou lost to The House. :(')
                    else:
                        print('\nIt was a tie!')
                        player.balance = player.balance + bet

            break
        # Single Game Loop end

        # Can you continue playing?
        if player.balance < minimumbet:
            print('\nYou have insufficient funds to keep playing. Better luck next time!')
            break

        # Want to continue playing?
        if replay():
            continue

        break

    # Table Loop end
    if input("\nGo back to Main Menu? (y/n) \n") == 'y':
        continue

    print('\n-----------------------------')
    print("-----Thanks for playing!-----")
    print('-----------------------------\n')
    playing = False
# Blackjack loop end
