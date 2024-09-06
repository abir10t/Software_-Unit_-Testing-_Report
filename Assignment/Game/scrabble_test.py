import unittest
from scrabble import scrabble_score, is_valid_word, word_length_is_correct

class TestScrabbleScore(unittest.TestCase):
    def test_empty_word(self):
        self.assertEqual(scrabble_score(""), 0)

    def test_single_letter(self):
        self.assertEqual(scrabble_score("A"), 1)

    def test_word_score(self):
        self.assertEqual(scrabble_score("cabbage"), 14)

    def test_mixed_case_word(self):
        self.assertEqual(scrabble_score("CaBbagE"), 14)

    def test_invalid_word(self):
        self.assertFalse(is_valid_word("xyz123"))

    def test_valid_word(self):
        self.assertTrue(is_valid_word("dog"))

    def test_word_length_check(self):
        self.assertTrue(word_length_is_correct("hello", 5))
        self.assertFalse(word_length_is_correct("hello", 3))

if __name__ == '__main__':
    unittest.main()