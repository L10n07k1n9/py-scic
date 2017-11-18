''' 
https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertAlmostEqual
https://www.youtube.com/watch?v=6tNS--WetLI 
'''
import unittest
import integral


class TestIntegral(unittest.TestCase):
    def test_integral(self):
        result = integral.Integral()
        self.assertGreaterEqual(result, 12)
        self.assertLessEqual(result, 13)

    def test_raiser(self):
        self.assertRaises(ValueError, integral.test_raise)


if __name__ == '__main__':
    unittest.main()
