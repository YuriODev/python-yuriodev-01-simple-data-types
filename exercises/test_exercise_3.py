import unittest
import subprocess

class TestExercise3(unittest.TestCase):
    def test_case_1(self):
        output = subprocess.check_output(['python3', 'exercise3.py'], input='3602\n', text=True)
        self.assertIn('1:00:02', output)

    def test_case_2(self):
        output = subprocess.check_output(['python3', 'exercise3.py'], input='4556789\n', text=True)
        self.assertIn('17:46:29', output)

    def test_case_3(self):
        output = subprocess.check_output(['python3', 'exercise3.py'], input='4568\n', text=True)
        self.assertIn('1:16:08', output)

if __name__ == '__main__':
    unittest.main()
