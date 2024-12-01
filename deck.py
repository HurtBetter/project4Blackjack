"""
The deck class makes the deck used for the game. This class was edited very little by us,
but nortably we added a deckAmount instance variable that is the amount of decks used in the game
"""


import random
from card import Card


class Deck():
   def __init__(self, deckAmount):
       self.cards = []
       self.deckAmount = deckAmount
       for i in range (deckAmount):
           for suit in Card.SUITS:
               for face in Card.FACES:
                   self.cards.append(Card(suit, face))


       random.shuffle(self.cards)


   def draw(self):
       if self.cards:
           return self.cards.pop()
       # reshuffle.
       newdeck = Deck(self.deckAmount)


       self.cards = newdeck.cards
       return self.draw()
