import unittest
import scic as s


class Test_scic(unittest.TestCase):
    def test_open_csv_metadata(self):
        r = s.open_csv_metadata("C:\\Users\\ld_la\\Google Drive\\IPN CIC MCC\\B17 MCC\\s1\\py\\lecture4\\people_data.csv")
        self.assertGreater(len(r), 0)
        self.assertGreater(r["lines"], 0)
        self.assertIsNotNone(r["data"]["header"])
        self.assertIsNotNone(r["data"]["rows"])
        self.assertEqual(r["status"],0)


if __name__ == '__main__':
    unittest.main()
