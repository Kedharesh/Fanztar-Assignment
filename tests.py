import unittest
from order_service import validate_order, calculate_total_price, create_order

class OrderServiceTests(unittest.TestCase):
    def test_validate_order(self):
        self.assertEqual(validate_order(["I", "A", "D", "F", "K"]), True)
        self.assertEqual(validate_order(["I", "A", "D", "F"]), False)  # Missing body
        self.assertEqual(validate_order(["I", "A", "D", "F", "K", "B"]), False)  # Duplicate screen

    def test_calculate_total_price(self):
        components = ["I", "A", "D", "F", "K"]
        expected_total = 42.31 + 10.28 + 25.94 + 18.77 + 45.00
        self.assertEqual(calculate_total_price(components), expected_total)

    def test_create_order(self):
        valid_order = ["I", "A", "D", "F", "K"]
        invalid_order = ["I", "A", "D", "F"]

        order = create_order(valid_order)
        self.assertEqual(order is not None, True)
        self.assertEqual("order_id" in order, True)
        self.assertEqual(len(order["parts"]), 5)
        self.assertEqual(sorted(order["parts"]), sorted(["LED Screen", "Wide-Angle Camera", "USB-C Port", "Android OS", "Metallic Body"]))
        self.assertAlmostEqual(order["total"], 142.3, places=2)

        self.assertEqual(create_order(invalid_order), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)