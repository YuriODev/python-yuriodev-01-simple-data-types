import unittest
import subprocess
import os
import ast

# Define the full path to the exercise script
exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_5.py")


class TestExample1(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_example_1(self):
        """Test the provided example 1."""
        output = self.run_exercise("8\n5\n")
        self.assertEqual(output, "8\n")

    def test_example_2(self):
        """Test the provided example 2."""
        output = self.run_exercise("5\n3\n")
        self.assertEqual(output, "5\n")

    def test_example_3(self):
        """Test the provided example 3."""
        output = self.run_exercise("7\n9\n")
        self.assertEqual(output, "9\n")

    def test_if_max_function_was_used(self):
        exercise_file_path = os.path.join(os.path.dirname(__file__),
                                          "exercise_5.py")
        with open(exercise_file_path, 'r') as file:
            file_content = file.read()
            self.assertNotIn(
                "max(", file_content,
                "You should not use the max function in your solution")


if __name__ == '__main__':
    unittest.main()
