
from carddeck import CardDeck

class Gamer:
    def __init__(self, id, chips):
        self.id = id
        self.chips = chips
        self.hands = []
    
    def WantCard(self, deck):
        if deck.CheckEmpty():
            deck = CardDeck()
            deck.Shuffle()
        
        card = deck.PopCard()
        self.hands.append(card)
    
    def ShowHand(self, reveal=True):
        
        if reveal == False:
            return [hand.rank+hand.suit for hand in self.hands][-1]
        
        return [hand.rank+hand.suit for hand in self.hands]
    
    def CalculateScore(self):
        if self.CountA() <= 1:
            hard_hand = self.HardHand()
            soft_hand = self.SoftHand()
            best_hand = self.BestHand(hard_hand, soft_hand)
        
        else:
            best_hand = self.BestHandMultipleAce()
        
        return best_hand
    
    def HardHand(self):
        hard_hand = 0
        
        for card in self.hands:
            face_value = '-x23456789TAJQK'.index(card.rank)
            if face_value > 11:
                hard_hand += 10
            
            else:
                hard_hand += face_value

        return hard_hand

    def SoftHand(self):
        soft_hand = 0
        
        for card in self.hands:
            face_value = '-A23456789TJQK'.index(card.rank)
            if face_value > 10:
                soft_hand += 10
            
            else:
                soft_hand += face_value
    
        return soft_hand

    def BestHand(self, hard_hand, soft_hand):
        if self.IsBust(hard_hand):
            return soft_hand
        
        else:
            return hard_hand
                
    def BestHandMultipleAce(self):
        ## try to count the first Ace as 11, and the remaining Ace as 1
        best_hand = 0
        count = 0
        
        for card in self.hands:
            if card.IsAce() and count == 0:
                best_hand += 11
                count += 1
            
            else:
                face_value = '-A23456789TJQK'.index(card.rank)
                if face_value > 11:
                    best_hand += 10
                else:
                    best_hand += face_value

        return best_hand

    def IsBust(self, score):
        return score > 21
    
    def CountA(self):
        num_A = 0
        for card in self.hands:
            if card.IsAce():
                num_A += 1
        
        return num_A
