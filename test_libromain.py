import unittest
from libromain import *

class TestLibRomain(unittest.TestCase):

    def test_romanize_dec(self):
        self.assertEqual(rocollect(romanize_dec(7)), 'VII', "Should be VII")
        self.assertEqual(rocollect(romanize_dec(4)), 'IV', "Should be IV")
        self.assertEqual(rocollect(romanize_dec(10)), 'X', "Should be X")
        self.assertEqual(rocollect(romanize_dec(1)), 'I', "Should be I")

    def test_romanize_beyond(self):
        self.assertEqual(rocollect(romanize_beyond(1337)), 'MCCCXXXVII', "Should be MCCCXXXVII")
        self.assertEqual(rocollect(romanize_beyond(81818)), 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDCCCXVIII', "Should be MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDCCCXVIII")
        self.assertEqual(rocollect(romanize_beyond(10000)), 'MMMMMMMMMM', "Should be MMMMMMMMMM")

if __name__ == '__main__':
    unittest.main()



