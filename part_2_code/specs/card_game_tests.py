import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("Hearts", 9)

    def test_card_has_suit(self):
        self.assertEqual("Hearts", self.card.suit)

    def test_card_has_value(self):
        self.assertEqual(9, self.card.value)

    def test_can_check_for_ace_false(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card))

    def test_can_check_for_ace_true(self):
        card = Card("Clubs", 1)
        self.assertEqual(True, CardGame.check_for_ace(self, card))

    def test_highest_card(self):
        card1 = Card("Spades", 7)
        card2 = Card("Diamonds", 3)
        self.assertEqual(card1, CardGame.highest_card(self, card1, card2))

    def test_cards_total(self):
        card1 = Card("Spades", 7)
        card2 = Card("Diamonds", 3)
        cards = [card1, card2]
        self.assertEqual("You have a total of 10", CardGame.cards_total(self, cards))

    
        

