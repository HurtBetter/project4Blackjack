"""
This class repreents the dealer for the game. We added an amountWon and gamesWon attribute to the dealer
to help us calclulate the house adavantage as well as give the total amount of games the dealer won.
"""


from hand import Hand
from player import Player


class Dealer:
   def __init__(self):
       self.hand = Hand()
       self.name = "Dealer"
       self.bet = 0
       self.bankroll = 1e7
       self.amountWon = 0
       self.gamesWon = 0


   def play_hand(self):
       if self.hand.value() < 17:
           return 'hit'
       return 'stand'


   def __str__(self):
       return "Dealer"
