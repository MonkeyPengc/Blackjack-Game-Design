# Blackjack Game Design in Python

Rules based on: http://www.bicyclecards.com/how-to-play/blackjack/

# Design Concepts

### Three Entities(Sub Entities)

Gamer(Dealer, Player)

CardDeck(Blackjack Card)

BlackjackManager(GameTable)

### Relation between Entities

A Dealer/Player is a Gamer.

A CardDeck has a specified amount of Cards.

A BlackjackManager has a GameTable.

### Behaviors of Entities

BlackjackManager shuffles the CardDeck when the system starts, or when there are 60 cards left.

BlackjackManager runs a GameTable, and decides the winner in each single play.

GameTable joins or leaves Gamers.

One Dealer and multiple Players play a CardDeck with their own strategies.

Dealer serves and deals with Players.

Players place bet, and make decisions in each single play.






