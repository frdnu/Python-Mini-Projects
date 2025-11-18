import random


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        self.cards = []
        for x in ("Hearts", "Diamonds", "Clubs", "Spades"):
            for y in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
                self.cards.append(Card(y, x))

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def _deal(self, num):
        count = self.count()
        if count == 0:
            raise ValueError("All cards have been dealt")

        actual = min(num, count)
        dealt_cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return dealt_cards

    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError('Only full decks can be shuffled')
        else:
            return random.shuffle(self.cards)

    def deal_card(self):
        single_card = self.cards[-1]
        self._deal(1)
        return single_card

    def deal_hand(self, num):
        return self._deal(num)


card = Card(3, 'spades')
print(card)
deck1 = Deck()


for x in deck1:
    print(x)
