import unittest
import reg_exp


class Test_ex(unittest.TestCase):
    def test_process(self):
        r = reg_exp.multiplos(3, 5)
        # multiplos(3,5)->[1,3,6,,9,12]
        self.assertEqual(r, [1, 3, 6, 9, 12])

if __name__ == '__main__':
    unittest.main()
