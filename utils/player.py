from card import Card
import random
from random import shuffle

#creating class player
class player:

    cards = []
    turn_count = 0
    number_of_cards = 0
    history = []

    def __init__(self, cards, turn_count, number_of_cards, history):

        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = []

    def play(self):
        random_card = random.choice(Card)
        self.history.append(random_card)
        print("{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}")
        return Card

#class Deck to get all 52 cards
class Deck(Card):

    def __init__(self):
        self.cards = []

    #fill_deck class to get all combination of icon, color, value =52 cards
    def fill_deck(self):
        color = ["black","red"]
        icon = ['♥','♦','♣','♠']
        value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        for c in color:
            for i in icon:
                for v in value:
                    if i in ["♣","♠"] and c == "Black":
                        card = Card(c,i,v)
                        self.cards.append(card)
                    else i in ["♥","♦"] and c == "Red":
                        card = Card(c,i,v)
                        self.cards.append(card)
        
    #print(len(Deck.cards))
        return self.cards
    #print(self.cards)

#deck = Deck()
#deck1 = deck.fill_deck()
#print(deck1)

#method to shuffel all cards in list'''
    def shuffle(self) -> list:
        random.shuffle(self.cards)
        return shuffle

    #print(self.cards)
    
    # to distribute cards to players
    def distribute(self, players:list):
        self.players = []
        for i in range (0, len(self.cards)):
            for player in players:
                if len(self.cards)>0:
                    card=self.cards[0]
                    player.cards.append(card)
                    self.cards=self.cards.remove(0)
