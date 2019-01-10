import unittest
from addition import addition

class myClass(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(4,5), (9))

if __name__ == "__main__":
    unittest.main()
