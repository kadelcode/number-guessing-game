import unittest
from unittest.mock import patch
from guess_the_number import generate_random_number, check_guess, guess_the_number

class TestGuessTheNumber(unittest.TestCase):
    def test_check_guess_too_low(self):
        """
        Tests if the guess is too low
        """
        self.assertEqual(check_guess(30, 6), "Too low!")

    def test_check_guess_to_high(self):
        """
        Tests if the guess is too high
        """
        self.assertEqual(check_guess(10, 25), "Too high!")

    def test_check_guess_correct(self):
        self.assertEqual(check_guess(25, 25), "Correct!")

    @patch('guess_the_number.generate_random_number', return_value=30)
    def test_guess_the_number_correct_guess(self, mock_generate_number):
        with patch('builtins.input', return_value='30'):
            with patch('builtins.print') as mock_print:
                guess_the_number()
                mock_print.assert_any_call("Correct!")
                mock_print.assert_any_call("Congratulations! You guessed the number in 1 attempts.")

if __name__ == "__main__":
    unittest.main()
