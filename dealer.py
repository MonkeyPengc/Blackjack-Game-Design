
from gamer import Gamer
from carddeck import CardDeck

class Dealer(Gamer):
    def __init__(self, id=5, chips=50000):
        Gamer.__init__(self, id, chips)
        self.chips = chips
    
    def HitOrStand(self, player):
        return player.MakeDecision()
    
    def CheckBigger17(self):
        soft_hand = self.SoftHand()
        hard_hand = self.HardHand()
        
        ## no A in hands
        if soft_hand == hard_hand:
            if hard_hand >= 17:
                return True
            
            else:
                return False
    
        ## all A in hands
        elif soft_hand == len(self.hands):
            return False
        
        ## not all A in hands
        else:
            if hard_hand < 17:
                return False
        
            else:
                num_A = self.CountA()
                if num_A == 1:
                    ## avoid bust, count the only Ace as 1
                    if hard_hand > 21 and soft_hand < 17:
                        return False
                
                    ## count the only Ace as 11, then hand in [17, 21]
                    return True
            
                else:
                    ## if the total is over 21, then need to deal with two cases
                    ## 1.if the soft hand is less than 17, return False
                    ## 2.if the soft hand is over 21, return True
                    ## else, need to deal with two cases
                    ## 1. if the total is less than 17, return False
                    ## 2. else return True
                    best_total = self.BestHandMultipleAce()
                    
                    if self.IsBust(best_total):
                        if soft_hand < 17:
                            return False
                        
                        if self.IsBust(soft_hand):
                            return True
                
                    else:
                        if best_total < 17:
                            return False
                        
                        return True

    def Deal(self, p, tie=False, player_win=False, player_natural=False):
        if tie:
            print("Player {0} takes back ${1} chips.".format(p.id, p.bet))
            p.chips += p.bet
            self.chips -= p.bet
        
        elif not player_win:
            print("Player {0} loses ${1} chips.".format(p.id, p.bet))
    
        ## player wins by 21, the dealer pays that player one and a half times the amount of his bet
        elif player_natural:
            print("Player {0} wins ${1} chips.".format(p.id, int(p.bet*1.5)))
            p.chips += p.bet*2.5
            self.chips -= p.bet*2.5
        
        ## player wins by a score higher than the dealer
        else:
            print("Player {0} wins ${1} chips.".format(p.id, p.bet))
            p.chips += p.bet*2
            self.chips -= p.bet*2
    
        p.play_status = False


