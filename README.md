Object Oriented Design Blackjack Game with AI in Python.

Rules based on http://www.bicyclecards.com/how-to-play/blackjack/

# Design Concepts

### Three Entities(Sub Entities)

Gamer(Dealer, Player)

CardDeck(Blackjack Card)

GameManager(GameTable)

### Relation between Entities

A Dealer/Player is a Gamer.

A CardDeck has a specified amount of Cards.

A GameManager has a GameTable.

### Behaviors of Entities

Dealer and Players play a CardDeck with their own strategies.

A GameTable has only 1 Dealer and may have up to 5 Players.

GameManager runs a GameTable and decides the winner in each single play.

One CardDeck contains 312 cards with 4 kinds of suit, 6 decks of standard 52-card pack are used.

Ace is worth 1 or 11. Face card are 10, and any other card is its pip value.

### Other Assumptions

At least 1 Dealer and 1 Player joins the GameTable in order to start the game.

Each participant places a bet in chips limited from $2 to $500.

GameManager reshuffles the CardDeck when the system starts, or when there are 60 cards left.
