import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

# Example usage:
if __name__ == "__main__":
    deck = Deck()
    print("Initial deck:")
    for card in deck.cards:
        print(card)

    print("\nShuffling deck...")
    deck.shuffle()

    print("\nShuffled deck:")
    for card in deck.cards:
        print(card)

    print("\nDealing a card:")
    card = deck.deal()
    if card:
        print("Dealt card:", card)
    else:
        print("Deck is empty")

