"""
The player class represents the player for the game. We added aan amountWon, gamesWon, and totalBet attribute
to the player class to help us calculate the house advantage and to tell us how many games the player won.
We did make some important changes to the player class, namely we fully automated and made it always follow basic strategy.
"""
from hand import Hand
from strategy import basic_strategy


class Player():
   def __init__(self, name, bankroll,betAmount):
       self.hand = Hand()
       self.bankroll = bankroll
       self.name = name
       self.bet = betAmount
       self.amountWon = 0
       self.gamesWon = 0
       self.totalBet = 0


   def play_hand(self, dealer_card):
       recommend = basic_strategy(self.hand.value(), dealer_card.value(), self.hand.is_soft())


       if len(self.hand.cards) == 2:
           pass


       else:
               # for simplicity. This is not true for soft 18.
           if recommend == 'double':
               recommend = 'hit'


       move = recommend


       if move.startswith('h'):
           return 'hit'
       elif move.startswith('s'):
           return 'stand'
       else:
           return 'double'




   def __str__(self):
       return '(%s, $%s)' % (self.name, self.bankroll)


   def is_bust(self):
       return self.hand.value() > 21
