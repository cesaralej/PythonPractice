import random
import time
from Deck import Deck
from Player import Player



playing = True
initialbalance = 5000
minimumbet = 200
winmultiplier = 2




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
