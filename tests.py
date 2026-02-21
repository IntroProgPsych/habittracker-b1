import unittest
from unittest.mock import patch
from app import interpret_score, get_valid_input

class Test_interptret_score(unittest.TestCase):
    
    def test_interpret_low(self):
        self.assertEqual(interpret_score(0), "Low")
        self.assertEqual(interpret_score(5), "Low")

    def test_interpret_moderate(self):
        self.assertEqual(interpret_score(6), "Moderate")
        self.assertEqual(interpret_score(8), "Moderate")

    def test_interpret_high(self):
        self.assertEqual(interpret_score(12), "High")
        self.assertEqual(interpret_score(21), "High")

class Test_get_valid_input(unittest.TestCase):
    @patch('builtins.input', return_value='5') 
    def test_valid_input_immediate(self, mock_input):
        result = get_valid_input("irrelevant text")
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['9', 'abc', '3'])
    def test_invalid_then_valid_input(self, mock_input):
        result = get_valid_input("irrelevant text")
        self.assertEqual(result, 3)

    @patch('builtins.input', return_value='0')
    def test_boundary_zero(self, mock_input):
        self.assertEqual(get_valid_input("irrelevant text"), 0)

    @patch('builtins.input', return_value='7')
    def test_boundary_seven(self, mock_input):
        self.assertEqual(get_valid_input("irrelevant text"), 7)

if __name__ == '__main__':
    unittest.main()