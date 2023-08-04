import unittest
import sys
sys.path.append("..")
from src.conversion_logic import Converter

class TestConverter(unittest.TestCase):

    def test_convert_unit(self):
        self.assertAlmostEqual(Converter.convert_unit(2.5, 10), 25.0, places=2)
        self.assertAlmostEqual(Converter.convert_unit(0.5, 20), 10.0, places=2)
        self.assertAlmostEqual(Converter.convert_unit(1.0, 100), 100.0, places=2)

        self.assertAlmostEqual(Converter.convert_unit(-3.0, 8), -24.0, places=2)
        self.assertAlmostEqual(Converter.convert_unit(-1.5, 12), -18.0, places=2)

        self.assertAlmostEqual(Converter.convert_unit(0.0, 50), 0.0, places=2)
        self.assertAlmostEqual(Converter.convert_unit(0.0, 1000), 0.0, places=2)

        self.assertAlmostEqual(Converter.convert_unit(2.5, -10), -25.0, places=2)
        self.assertAlmostEqual(Converter.convert_unit(0.5, -20), -10.0, places=2)

        self.assertAlmostEqual(Converter.convert_unit(0.0, -50), 0.0, places=2)
        self.assertAlmostEqual(Converter.convert_unit(0.0, -1000), 0.0, places=2)

if __name__ == "__main__":
    unittest.main()
