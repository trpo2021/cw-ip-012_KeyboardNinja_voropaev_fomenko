import unittest
from importlib import reload
import main
import difficulty


class TKinterMainWindowTest(unittest.TestCase):
    def setUp(self):
        reload(main)

    def test_get_one_word(self):
        self.assertEqual(len(difficulty.get_words(1)), 1)

    def test_get_two_words(self):
        self.assertEqual(len(difficulty.get_words(2)), 2)

    def test_get_three_words(self):
        self.assertEqual(len(difficulty.get_words(3)), 3)

    def test_key_type_parameters(self):
        self.assertRaises(AttributeError, difficulty.key_type, 15)

    def test_main_root(self):
        second_win = difficulty.dif(difficulty.get_words(1))
        self.assertEqual(len(second_win.children), 2)
        self.assertIn('!text', second_win.children)
        second_win = difficulty.dif(difficulty.get_words(3))
        self.assertEqual(len(second_win.children), 2)
        self.assertIn('!text', second_win.children)


if __name__ == '__main__':
    unittest.main()
