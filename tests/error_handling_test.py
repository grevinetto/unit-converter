import unittest
import sys
sys.path.append("..")
from src.error_handling import BaseValidator, ErrorHandling, ValidationError

class TestErrorHandling(unittest.TestCase):

    def test_is_numeric_valid(self):
        self.assertTrue(BaseValidator.is_numeric("123.45"))
        self.assertTrue(BaseValidator.is_numeric("-67.89"))
        self.assertTrue(BaseValidator.is_numeric("0"))

    def test_is_numeric_invalid(self):
        self.assertFalse(BaseValidator.is_numeric("abc"))
        self.assertFalse(BaseValidator.is_numeric("12.34.56"))
        self.assertFalse(BaseValidator.is_numeric("1,000"))

    def test_validate_numeric_input_valid(self):
        self.assertEqual(BaseValidator.validate_numeric_input("123.45"), 123.45)
        self.assertEqual(BaseValidator.validate_numeric_input("-67.89"), -67.89)

    def test_validate_numeric_input_invalid(self):
        with self.assertRaises(ValidationError):
            BaseValidator.validate_numeric_input("")
        with self.assertRaises(ValidationError):
            BaseValidator.validate_numeric_input("abc")
        with self.assertRaises(ValidationError):
            BaseValidator.validate_numeric_input("1,000")

    def test_validate_numeric_range_valid(self):
        self.assertIsNone(BaseValidator.validate_numeric_range(5, 0, 10))
        self.assertIsNone(BaseValidator.validate_numeric_range(-2.5, -5, 5))

    def test_validate_numeric_range_invalid(self):
        with self.assertRaises(ValidationError):
            BaseValidator.validate_numeric_range(15, 0, 10)
        with self.assertRaises(ValidationError):
            BaseValidator.validate_numeric_range(-10, 0, 5)

    def test_validate_temperature_range_valid(self):
        self.assertIsNone(ErrorHandling.validate_temperature_range("Celsius", 25))
        self.assertIsNone(ErrorHandling.validate_temperature_range("Fahrenheit", 80))

    def test_validate_temperature_range_invalid(self):
        with self.assertRaises(ValidationError):
            ErrorHandling.validate_temperature_range("Celsius", -300)
        with self.assertRaises(ValidationError):
            ErrorHandling.validate_temperature_range("Fahrenheit", 2000)

if __name__ == "__main__":
    unittest.main()
