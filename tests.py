import unittest
from app import interpret_score

class TestHabitTracker(unittest.TestCase):
    
    def test_interpret_low(self):
        """Test that scores less than 6 return 'Low'"""
        self.assertEqual(interpret_score(0), "Low")
        self.assertEqual(interpret_score(5), "Low")

    def test_interpret_moderate(self):
        """Test that scores between 6 and 11 return 'Moderate'"""
        self.assertEqual(interpret_score(6), "Moderate")  # Boundary check
        self.assertEqual(interpret_score(8), "Moderate")
        self.assertEqual(interpret_score(11), "Moderate") # Boundary check

    def test_interpret_high(self):
        """Test that scores 12 or higher return 'High'"""
        self.assertEqual(interpret_score(12), "High")     # Boundary check
        self.assertEqual(interpret_score(21), "High")     # Max possible score (3 questions * 7 days)

if __name__ == '__main__':
    unittest.main()