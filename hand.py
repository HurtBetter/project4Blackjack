"""
The hand class represents the hand that a player/dealer has.
"""


class Hand:
   def __init__(self):
       self.cards = []


   def is_soft(self):
       value = 0
       has_ace = False


       for card in self.cards:
           if card.is_ace():
               has_ace = True


           value += card.value()


       return has_ace and value <= 11


   def value(self):
       value = 0
       has_ace = False


       for card in self.cards:
           value += card.value()


           if card.is_ace():
               has_ace = True


       if has_ace and value <= 11:
           value += 10


       return value
