conversion_data = {
    'Watt': {
        'Watt': 1,
        'Kilowatt': 0.001,
        'Megawatt': 1e-6,
        'Horsepower': 0.00134102,
        'Btu Per Hour': 3.41214,
    },
    'Kilowatt': {
        'Watt': 1000,
        'Kilowatt': 1,
        'Megawatt': 0.001,
        'Horsepower': 1.34102,
        'Btu Per Hour': 3412.14,
    },
    'Megawatt': {
        'Watt': 1e+6,
        'Kilowatt': 1000,
        'Megawatt': 1,
        'Horsepower': 1341.02,
        'Btu Per Hour': 3.41214e+6,
    },
    'Horsepower': {
        'Watt': 745.7,
        'Kilowatt': 0.7457,
        'Megawatt': 7.457e-4,
        'Horsepower': 1,
        'Btu Per Hour': 2544.43,
    },
    'Btu Per Hour': {
        'Watt': 0.293071,
        'Kilowatt': 2.93071e-4,
        'Megawatt': 2.93071e-7,
        'Horsepower': 3.9301e-4,
        'Btu Per Hour': 1,
    },
    # Add more units and their conversion factors as needed
}
