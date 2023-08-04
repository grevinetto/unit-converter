from callerfunction import Caller
from conversion_logic import Converter
from error_handling import ValidationError, BaseValidator, ErrorHandling

test = Caller()
print("Available categories:", test.categories)
user_input_category = input("Enter a category to call the associated dictionary: ")
dictionary_category = test.call_dictionary(user_input_category)

if dictionary_category:
    print("Dictionary loaded for category:", user_input_category)
    print("Available units:", list(dictionary_category.keys()))

    user_input_starting_unit = input("Select a starting unit: ")
    if user_input_starting_unit in dictionary_category:
        user_input_target_unit = input("Select the target unit to get the conversion factor: ")
        if user_input_target_unit in dictionary_category:
            conversion_factor = dictionary_category[user_input_starting_unit][user_input_target_unit]
            print(f"Conversion factor from {user_input_starting_unit} to {user_input_target_unit}: {conversion_factor}")
            starting_value = float(input("Provide a value to be converted: "))
            print(Converter.convert_unit(conversion_factor, starting_value))
        else:
            print("Invalid target unit. Please choose from the available units.")
    else:
        print("Invalid starting unit. Please choose from the available units.")
else:
    print("Invalid category. Please choose from the available categories.")
