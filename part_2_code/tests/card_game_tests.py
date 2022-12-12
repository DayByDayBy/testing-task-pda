import unittest
from src.card import Card
from src.card_game import CardGame



class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card("heart", 1)
        self.card2 = Card("heart", 3)


    def test_check_for_ace(self):
        expected = True
        outcome = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(expected, outcome)
        

    def test_highest_card(self):
        expected = self.card2
        actual = self.cardgame.highest_card(self.card1, self.card2)
        self.assertEqual(expected, actual) 
    
        
    def test_cards_total(self):
        cards = [self.card1, self.card2]
        expected_total = ('You have a total of 4')
        actual = self.cardgame.cards_total(cards)
        self.assertEqual(expected_total, actual)
            



