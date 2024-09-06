import unittest
from scrabble import scrabble_score

class TestScrabbleScore(unittest.TestCase):
    def test_word_score(self):
        self.assertEqual(scrabble_score("cabbage"), 14)

if __name__ == '__main__':
    unittest.main()