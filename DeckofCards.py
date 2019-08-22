from random import shuffle

class Card:

    def __init__(self, value, suite):
        self.value = value
        self.suite = suite

    def __repr__(self):
        return f"{self.value} of {self.suite}"


class Deck:

    def __init__(self):  # no need for other parameter as it will always return a deck of 52 cards
        allowed_suite = ["Hearts", "Diamonds", "Clubs", "Spades"]
        allowed_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suite) for suite in allowed_suite for value in allowed_value]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def _deal(self,how_many):
        count=self.count()
        actual = min([how_many, count])  # we may need to remove less than how_many if not enough cards left in the deck
        if count == 0:
            raise ValueError("All cards have been dealt.")
        cards = self.cards[-actual:]    #get this many from the end of the list
     #   print("Cards ", cards)
        self.cards = self.cards[:-actual]   #deck list is not from 0 to : this many from the end of the list
      #  print("\nself.cards ", self.count(), self.cards)
        return cards

    def shuffle(self):
        count = self.count()
        if count != 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)   #this is the random.shuffle method)
        return self  #you don't have to "return self" but it is good practice

    def deal_card(self):
        one_card= self._deal(1)[0]   # [0] because we return the card, not the list consisting of that 1 card
        return one_card

    def deal_hand(self, how_many):
        hand=self._deal(how_many)
        return hand


# #c=Card("10","Hearts")
#
# d=Deck()
# #print(d._deal(5))
# print(d)
# print(d.cards)
#
# d.shuffle()
# #print(shuffled._deal(5))
# print(d.deal_card())
# print("\n", d.count(), d.cards)
# print(d.deal_hand(4))
# print("\n", d.count(), d.cards)
#
# #d.shuffle()
# shuffled=Deck()
# print(shuffled)
#
# iterate_cards = d
# for card in iterate_cards:
#     print(card)
#
#
