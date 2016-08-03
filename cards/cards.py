from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = []
    suits = []

    def __init__(self):
        self._deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._deck)

    def __getitem__(self, position):
        return self._deck[position]

class FrenchDeck(Deck):
    ranks = [str(n) for n in range(2,10)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

class SerengethiDeck(Deck):
    ranks = [str(n) for n in range(1,6)]
    suits = 'lion elephant hippopotamus crocodile giraffe buffalo eland'.split()
