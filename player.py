from gamer import Gamer
from carddeck import CardDeck

class Player(Gamer):
    def __init__(self, id, chips):
        Gamer.__init__(self, id, chips)
        self.bet = 0
        self.play_status = True
    
    def PlaceBet(self, dealer, bet):
        self.chips -= bet
        self.bet = bet
        dealer.chips += bet
    
    def MakeDecision(self):
        choice = input("Press 'h' to Hit, or any button to Stand: ")
        return choice.lower() == 'h'
    
    def PlayAgain(self):
        choice = input("Player {}, press 'p' to Play again, or any button to Leave: ".format(self.id))
        return choice.lower() == 'p'
