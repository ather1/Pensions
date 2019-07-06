import unittest

from prime import is_prime

class Tests(unittest.TestCase):
    def test1(self):
        self.assertFalse(is_prime(11))

    def test23(self):
        self.assertTrue(is_prime(23))


    def test8(self):
        self.assertFalse(is_prime(8))

if __name__ == "__main__":
    unittest.main() 
     