import unittest

from eulpy01 import compute

class eulpy01Test(unittest.TestCase):
    def test_result(self):
        """
        Test that it can sum a list of integers
        """
        result = compute()
        self.assertEqual(result, '23331668')
        print("eulpy01Test passed")

if __name__ == '__main__':
    unittest.main()