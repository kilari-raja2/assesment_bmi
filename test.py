import json
from bmi_calculator import bmi_calc

test_data,overweight_count = bmi_calc('data.json')
print(test_data)