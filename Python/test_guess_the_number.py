import unittest
from unittest.mock import patch
from guess_the_number import generate_random_number, check_guess

class TestGuessTheNumber(unittest.TestCase):
    def test_check_guess_too_low(self):
        """
        Tests if the guess is too low
        """
        self.assertEqual(check_guess(30, 6), "Too low!")

if __name__ == "__main__":
    unittest.main()
