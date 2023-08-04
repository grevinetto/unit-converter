import streamlit as st
from callerfunction import Caller
from conversion_logic import Converter
from error_handling import ErrorHandling, ValidationError


def main():
    caller = Caller()

    st.title("Unit Converter App")
    
    # Dropdown menu to select the category
    selected_category = st.selectbox("Select a category", caller.categories)

    if selected_category:
        st.write("Selected category:", selected_category)

        # Load the dictionary for the selected category
        dictionary_category = caller.call_dictionary(selected_category)

        # Dropdown menu to select the starting unit
        selected_starting_unit = st.selectbox("Select a starting unit", list(dictionary_category.keys()))

        if selected_starting_unit:
            st.write("Selected starting unit:", selected_starting_unit)

            # Dropdown menu to select the target unit
            selected_target_unit = st.selectbox("Select a target unit", list(dictionary_category.keys()))

            if selected_target_unit:
                st.write("Selected target unit:", selected_target_unit)

                # Show the conversion factor
                conversion_factor = dictionary_category[selected_starting_unit][selected_target_unit]
                st.write(f"Conversion factor from {selected_starting_unit} to {selected_target_unit}: {conversion_factor:.4f}")

                if selected_category == "Linear Expansion Coefficient":
                    input_value = st.text_input("Enter the starting value:", "0")

                    # Validate the input value for temperature ranges
                    try:
                        ErrorHandling.validate_temperature_range(selected_starting_unit, float(input_value))
                    except ValidationError as ve:
                        st.error(str(ve))
                        return
                else:
                    input_value = st.text_input("Enter the starting value:", "0")

                    # Validate the input value for numeric ranges
                    if not ErrorHandling.is_numeric(input_value):
                        st.error("Invalid input. Please enter a valid numeric value.")
                        return

                starting_value = float(input_value)

                # Add a conversion button that the user can click to trigger the conversion
                if st.button("Convert"):
                    Converter.convert_unit(conversion_factor, starting_value)
                    st.write(f"Conversion of {starting_value} from {selected_starting_unit} to {selected_target_unit}: {Converter.convert_unit(conversion_factor, starting_value):,}")
                


if __name__ == "__main__":
    main()