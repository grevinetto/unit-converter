class ValidationError(Exception):
    pass

class BaseValidator:

    @staticmethod
    def is_numeric(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    # @staticmethod
    # def validate_numeric_input(input_value):
    #     if not BaseValidator.is_numeric(input_value):
    #         raise ValidationError("Invalid input. Please enter a valid numeric value.")
    #     return float(input_value)

    @staticmethod
    def validate_numeric_range(input_value, min_value, max_value):
        if input_value < min_value or input_value > max_value:
            raise ValidationError(f"Invalid input. Please enter a value between {min_value} and {max_value}.")

class ErrorHandling(BaseValidator):

    @staticmethod
    def validate_temperature_range(selected_unit, input_value):
        temperature_ranges = {
            "Per Celsius": {"min": -273.15, "max": 1000.0},
            "Per Fahrenheit": {"min": -459.67, "max": 1832.0},
            "Per Kelvin": {"min": 0.0, "max": 1273.15}
        }

        if selected_unit in temperature_ranges:
            validation_range = temperature_ranges[selected_unit]
            BaseValidator.validate_numeric_range(input_value, validation_range["min"], validation_range["max"])
   