import unittest
import ex


class Test_ex(unittest.TestCase):
    def test_multiplos(self):
        r = ex.multiplos(3, 5)
        # multiplos(3,5)->[1,3,6,,9,12]
        self.assertEqual(r, [1, 3, 6, 9, 12])

    def test_criba(self):
        A=[1,2,3,4,5,6,7,8,9,10,11,12]
        r = ex.criba(3,A)
        self.assertEqual(r, [1,2,0,4,5,0,7,8,0,10,11,0])

if __name__ == '__main__':
    unittest.main()
