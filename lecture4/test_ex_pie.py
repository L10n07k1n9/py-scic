import unittest
import ex_pie as pie


class Test_ex_pie(unittest.TestCase):
    def test_open_csv_metadata(self):
        r = pie.plot_from_csv(
            "C:\\Users\\ld_la\\Google Drive\\IPN CIC MCC\\B17 MCC\\s1\\py\\lecture4\\people_data.csv")
        self.assertEqual(r, 0)


if __name__ == '__main__':
    unittest.main()
