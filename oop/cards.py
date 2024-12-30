ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♡", "♢", "♣"]


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

        self.value = Card.calc_value(self.rank)

    @staticmethod
    def calc_value(rank: str) -> int:
        if rank in ["J", "Q", "K"]:
            return 10
        elif rank == "A":
            return 11
        else:
            return int(rank)

    def __str__(self):
        return f"{self.rank} {self.value}"


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        import random

        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __str__(self):
        return f"{self.cards}"


deck = Deck()
deck.shuffle()
card = deck.deal()
print(card)
