import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

##############################################################


class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of '+self.suit

############################################################


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                # Storing all 52 cards in all_cards
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#############################################################


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def add_card(self, new_cards):

        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def remove_card(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


#############################################################
# three_cloves = Card("Clubs", "Three")

# mycard = new_deck.deal_one()
# arpan = Player("Arpan")
# arpan.add_card([mycard, mycard, mycard])
# print(arpan)


# for card in new_deck.all_cards:
#     print(card)


# print(three_cloves.value)
#
'''
Game logic:-  At first we have to create two players using player class the we create a deck of cards and shuffle ,after that we have to divide 26 cards to each player . After that we will we 
set an while loop game_on while game on is true the game will continue inside the while check contineoulsy about no cards each player has whwn one player has zero cards then that player will and other will win and the game_on will be turn to false and will break out of the loop

Evaluation:-


'''
player_one = Player("ONE")
player_two = Player("TWO")

new_deck = Deck()
new_deck.shuffle()


# Dividing the cards between two players

for i in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

game_on = True
rounds = 0
while game_on:
    rounds += 1
    print(f'{rounds} are played')

    if(len(player_one.all_cards) == 0):
        print('Player has no cards left')
        print('Player Two has won')
        game_on = False
        break

    if(len(player_two.all_cards) == 0):
        print('Player has no cards left')
        print('Player Two has won')
        game_on = False
        break
    # round
    player_one_cards = []
    player_two_cards = []

    player_one_cards.append(player_one.remove_card())
    player_two_cards.append(player_two.remove_card())

    war = True

    while war:
        if(player_one_cards[-1].value > player_two_cards[-1].value):
            print('PLAYER ONE HAS WON THIS ROUND')
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            war = False
        elif(player_two_cards[-1].value > player_one_cards[-1].value):
            print('PLAYER TWO HAS WON THIS ROUND')
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            war = False
        else:
            print('WAR!!!!!!!!!!')
            if (len(player_one.all_cards) < 10):
                print('unable to play has less cards')
                print('PLAYER TWO HAS WON')
                game_on = False
                break
            elif (len(player_two.all_cards) < 10):
                print('unable to play has less cards')
                print('PLAYER ONE HAS WON')
                game_on = False
                break

            else:
                for i in range(10):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
