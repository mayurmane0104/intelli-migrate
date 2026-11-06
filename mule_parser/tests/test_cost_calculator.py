import unittest
from mule_parser.utils.cost_calculator import calculate_nova_cost

class TestCostCalculator(unittest.TestCase):
    def test_calculate_nova_cost(self):
        # 1M input tokens = $0.06
        self.assertAlmostEqual(calculate_nova_cost(1_000_000, 0), 0.06)
        # 1M output tokens = $0.24
        self.assertAlmostEqual(calculate_nova_cost(0, 1_000_000), 0.24)
        # Both
        self.assertAlmostEqual(calculate_nova_cost(1_000_000, 1_000_000), 0.30)
        # Fractions
        self.assertAlmostEqual(calculate_nova_cost(500_000, 250_000), 0.09)

if __name__ == '__main__':
    unittest.main()
