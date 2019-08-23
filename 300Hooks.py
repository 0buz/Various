import unittest
from DeckofCards import Card, Deck


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.testdeck = Deck()

    def test_count(self):
        """Count"""
        self.testdeck.count()
        self.assertEqual(self.testdeck.count(), 52)
        self.testdeck.cards.pop()
        self.assertEqual(self.testdeck.count(), 51)
 



if __name__=="__main__":
    unittest.main()