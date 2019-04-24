import random
import time
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
WAIT_TIME = 0.3

class HouseBustException(Exception):
    """Exception raised when the house is bust."""
    pass

class PlayerBustException(Exception):
    """Exception raised when the player is bust."""
    pass

class Deck:
    
    def __init__(self):
        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards = self.cards + [(rank, suit)];

    def shuffle(self):
        random.shuffle(self.cards);

    def deal(self):
        return self.cards.pop();

    def __str__(self):
        deckstring = "This is your deck:\n"

        for card in self.cards:
            deckstring +=  f"${card[0]} of ${card[1]}\n"

        return deckstring
        

class Player:

    def __init__ (self, balance, house = False):
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
                        print (f"The minimum bet is {minbet}, please enter a higher amount of money!")
                else:
                    print ("Funds Unavailable, please enter a lower amount of money!")
                    continue
            except ValueError:
                print("Only use numbers!")
                continue

    def resethand(self):
        self.hand = []
        self.aces = 0

    def calculatevalue(self):
        self.value = 0
        for card in self.hand:
            self.value = self.value + VALUES[card[0]]
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
            if len(self.hand)>0:
                time.sleep(WAIT_TIME)
                for card in self.hand:
                    print(f'--{card[0]} of {card[1]}')
                    time.sleep(WAIT_TIME)
            else:
                print("There are no cards on your hand")

        else:
            print("\nThe House's hand is: ")
            time.sleep(WAIT_TIME)
            for card in self.hand:
                print(f'--{card[0]} of {card[1]}')
                time.sleep(WAIT_TIME)

class Game(object):
    """Class responsible for running the game"""
    def __init__(self, minimumbet = 200, winmultiplier = 2):
        self.minimumbet = minimumbet
        self.winmultiplier = winmultiplier
        self.deck = Deck()
        self.player = None
        self.house = None

    def set_table(self, player, house):
        """ Initialize the table """
        self.deck = Deck()
        self.deck.shuffle()
        self.player = player
        self.house = house

        #Reset Player Hand    
        self.player.resethand()
        self.house.resethand()

        return self.deck

        
    #Ask for replay
    def replay(self):    
        return input('\nDo you want to play again? (y/n) \n') == ('y')

    def draw_hands(self):
        """Draw the hands for the player and the house """
        self.bet = self.player.bet(self.minimumbet)

        #initial house draw
        self.house.draw(self.deck.deal())
        self.house.draw(self.deck.deal())
        self.house.calculatevalue()
        self.house.showhand()

        #initial player draw
        self.player.draw(self.deck.deal())
        self.player.draw(self.deck.deal())
        self.player.calculatevalue()
        self.player.showhand()

    def player_plays(self):
        """ Player loop logic"""
        while not self.player.bust():
            move = input('\nHit or stand? (h/s) \n')

            if move.lower() == ('h'):
                newcard = self.deck.deal()
                self.player.draw(newcard)
                self.player.calculatevalue()
                time.sleep(WAIT_TIME)
                print('\nYour new card is...')
                time.sleep(WAIT_TIME)
                print(f'--{newcard[0]} of {newcard[1]}')
                continue

            elif move.lower() == ('s'):
                break

            #Incorrect input
            else:
                print('Please insert a valid input.')
        
        if self.player.bust():
            raise PlayerBustException("Player is Bust!")

    def house_plays(self):
        """ House loop """
        while self.house.value <= 17:
            newcard = self.deck.deal()
            self.house.draw(newcard)
            self.house.calculatevalue()
            time.sleep(WAIT_TIME)
            print("\nThe House's new card is...")
            time.sleep(WAIT_TIME)
            print(f'--{newcard[0]} of {newcard[1]}')
            
            if self.house.bust():
                raise HouseBustException("House is bust!")




def main(initialbalance = 5000, minimumbet = 200, winmultiplier = 2):
    """ Main game loop """
    playing = True
    #Blackjack loop
    game  = Game(minimumbet, winmultiplier)

    while playing:
        print ('\n-----------------------------') 
        print ('----Welcome to Blackjack!----') 
        print ('-----------------------------' ) 
        if input ('\nWant to learn how to play? (y/n) \n') == 'y':
            print ("\nYou'll start with $5000, Press s to stand or h to hit")
            playing = False
            break

        input ('\nPress Enter to start!')

        player = Player(initialbalance)
        house = Player(initialbalance*10, True)

        while True:
            while True:
                if player.balance < minimumbet:
                    print('\nYou have insufficient funds to keep playing. Better luck next time!')
                    break

                try:
                    deck = game.set_table(player, house)

                    bust = False
                    print ('\n----------New Game!----------') 

                    game.draw_hands()

                    # TODO: catch exceptions
                    
                    game.player_plays()

                    game.house_plays()

                    print("Concluding game...")
                    time.sleep(WAIT_TIME)
                    if house.value < player.value:
                        player.win(bet*winmultiplier)
                    elif house.value > player.value:
                        print('\nYou lost to The House. :(')
                    else:
                        print('\nIt was a tie!')
                        player.balance = player.balance+bet
                except HouseBustException as e:
                    print(str(e))
                    player.win(game.bet*winmultiplier)
                except PlayerBustException as e:
                    print(str(e))

                #Want to continue playing?
                if game.replay():
                    continue
            break
              
        #Table Loop end
        if input("\nGo back to Main Menu? (y/n) \n") == 'y':
            continue
        else:
            playing = False

        print('\n-----------------------------') 
        print("-----Thanks for playing!-----")
        print('-----------------------------\n' ) 
        

if __name__ == '__main__':
    main()