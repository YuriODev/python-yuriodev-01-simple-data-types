import unittest
import subprocess
import os

# Define the full path to the exercise script
exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_11.py")


class TestBillDenominations(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_example_1(self):
        """Test the provided example 1."""
        output = self.run_exercise("534\n")
        self.assertIn("1 (500)", output)
        self.assertIn("0 (100)", output)
        self.assertIn("3 (10)", output)
        self.assertIn("0 (5)", output)
        self.assertIn("4 (1)", output)

    def test_example_2(self):
        """Test the provided example 2."""
        output = self.run_exercise("1245\n")
        self.assertIn("2 (500)", output)
        self.assertIn("2 (100)", output)
        self.assertIn("4 (10)", output)
        self.assertIn("1 (5)", output)
        self.assertIn("0 (1)", output)

    def test_example_3(self):
        """Test the provided example 3."""
        output = self.run_exercise("12\n")
        self.assertIn("0 (500)", output)
        self.assertIn("0 (100)", output)
        self.assertIn("1 (10)", output)
        self.assertIn("0 (5)", output)
        self.assertIn("2 (1)", output)

    def test_example_4(self):
        """Test the provided example 4."""
        output = self.run_exercise("786\n")
        self.assertIn("1 (500)", output)
        self.assertIn("2 (100)", output)
        self.assertIn("8 (10)", output)
        self.assertIn("1 (5)", output)
        self.assertIn("1 (1)", output)

    def test_example_5(self):
        """Test the provided example 5."""
        output = self.run_exercise("377\n")
        self.assertIn("0 (500)", output)
        self.assertIn("3 (100)", output)
        self.assertIn("7 (10)", output)
        self.assertIn("1 (5)", output)
        self.assertIn("2 (1)", output)




if __name__ == '__main__':
    unittest.main()