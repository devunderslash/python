import unittest

from eulpy25 import compute

class eulpy01Test(unittest.TestCase):
    def test_result(self):
        """
        Test that it can return the 1000 digit
        """
        result = compute()
        self.assertEqual(result, '4782')
        print("eulpy25Test passed")

if __name__ == '__main__':
    unittest.main()