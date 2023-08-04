import unittest
import sys
sys.path.append("..")
from src.callerfunction import Caller

class TestCaller(unittest.TestCase):
    def setUp(self):
        self.caller = Caller()

    def test_get_available_categories(self):
        expected_categories = ["Acceleration", "Area", "Concentration", 
                               "Energy", "Flow Rate", 
                               "Force", "Fuel Efficiency", "Length",
                               "Linear Expansion Coefficient", "Mass",
                               "Moment Of Mass", "Power", "Pressure",
                               "Velocity", "Volume"]
        actual_categories = sorted(self.caller.get_available_categories())
        self.assertListEqual(actual_categories, expected_categories)

    def test_call_dictionary(self):
        category = "Length"
        expected_dictionary = {'Meter': {
        'Meter': 1,
        'Centimeter': 100,
        'Millimeter': 1000,
        'Micrometer': 1e+6,
        'Nanometer': 1e+9,
        'Mile': 0.000621371,
        'Yard': 1.09361,
        'Foot': 3.28084,
        'Inch': 39.3701,
        },
        'Centimeter': {
            'Meter': 0.01,
            'Centimeter': 1,
            'Millimeter': 10,
            'Micrometer': 10000,
            'Nanometer': 1e+7,
            'Mile': 6.21371e-6,
            'Yard': 0.0109361,
            'Foot': 0.0328084,
            'Inch': 0.393701,
        },
        'Millimeter': {
            'Meter': 0.001,
            'Centimeter': 0.1,
            'Millimeter': 1,
            'Micrometer': 1000,
            'Nanometer': 1e+6,
            'Mile': 6.21371e-7,
            'Yard': 0.00109361,
            'Foot': 0.00328084,
            'Inch': 0.0393701,
        },
        'Micrometer': {
            'Meter': 1e-6,
            'Centimeter': 1e-4,
            'Millimeter': 0.001,
            'Micrometer': 1,
            'Nanometer': 1000,
            'Mile': 6.21371e-10,
            'Yard': 1.09361e-6,
            'Foot': 3.28084e-6,
            'Inch': 3.93701e-5,
        },
        'Nanometer': {
            'Meter': 1e-9,
            'Centimeter': 1e-7,
            'Millimeter': 1e-6,
            'Micrometer': 0.001,
            'Nanometer': 1,
            'Mile': 6.21371e-13,
            'Yard': 1.09361e-9,
            'Foot': 3.28084e-9,
            'Inch': 3.93701e-8,
        },
        'Mile': {
            'Meter': 1609.34,
            'Centimeter': 160934,
            'Millimeter': 1.609e+6,
            'Micrometer': 1.609e+9,
            'Nanometer': 1.609e+12,
            'Mile': 1,
            'Yard': 1760,
            'Foot': 5280,
            'Inch': 63360,
        },
        'Yard': {
            'Meter': 0.9144,
            'Centimeter': 91.44,
            'Millimeter': 914.4,
            'Micrometer': 914400,
            'Nanometer': 9.144e+8,
            'Mile': 0.000568182,
            'Yard': 1,
            'Foot': 3,
            'Inch': 36,
        },
        'Foot': {
            'Meter': 0.3048,
            'Centimeter': 30.48,
            'Millimeter': 304.8,
            'Micrometer': 304800,
            'Nanometer': 3.048e+8,
            'Mile': 0.000189394,
            'Yard': 0.333333,
            'Foot': 1,
            'Inch': 12,
        },
        'Inch': {
            'Meter': 0.0254,
            'Centimeter': 2.54,
            'Millimeter': 25.4,
            'Micrometer': 25400,
            'Nanometer': 2.54e+7,
            'Mile': 1.5783e-5,
            'Yard': 0.0277778,
            'Foot': 0.0833333,
            'Inch': 1,
        },
    }
        actual_dictionary = self.caller.call_dictionary(category)
        self.assertDictEqual(actual_dictionary, expected_dictionary)

if __name__ == "__main__":
    unittest.main()