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
<<<<<<< HEAD
        # ... и это текстовое поле
        self.assertIn('!text', second_win.children)


class TopLevelTest(unittest.TestCase):
    def setUp(self):
        reload(main)

    def test_top(self):
        self.assertEqual(len(main.top.children), 10)
        children_dct = main.top.children
        self.assertIn('!radiobutton', children_dct)
        self.assertIn('!radiobutton2', children_dct)
        self.assertIn('!radiobutton3', children_dct)
        self.assertIn('!button', children_dct)
        self.assertIn('!button2', children_dct)
        self.assertIn('!label', children_dct)
        self.assertIn('!label5', children_dct)
        self.assertIn('!label2', children_dct)
        self.assertIn('!label3', children_dct)
        self.assertIn('!label4', children_dct)


=======
        self.assertIn('!text', second_win.children)


>>>>>>> f902508818b51d106d8b1ca63b9a87c7adda2e91
if __name__ == '__main__':
    unittest.main()
