import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("hearts", 4)
        self.card2 = Card("spades", 8)
        self.cards = CardGame([self.card1,self.card2])


    # @unittest.skip       
    def test_if_card_is_ace(self): 
        self.assertEqual(False, self.cards.check_for_ace(self.card1))    

    # @unittest.skip
    def test_for_highest_card(self):
        self.assertEqual(self.card2, self.cards.highest_card(self.card1, self.card2) )

    # @unittest.skip
    def test_for_total_cards_value(self):
        total_cards = self.card1, self.card2
        self.assertEqual("You have a total of 12", self.cards.cards_total(total_cards))

    