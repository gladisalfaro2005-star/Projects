# Problem 1: Temperature converter and range flag
# Description: Converts a temperature from Celsius to Fahrenheit and Kelvin.
# Also checks if the temperature is considered high.
# Inputs:
# - temp_c (float)
# Outputs:
# - Fahrenheit value
# - Kelvin value
# - High temperature boolean
# Validations:
# - temp_c must be a valid float
# - temp_c must be >= -273.15
# Test cases:
# 1) Normal: 25 -> 77.0 F, 298.15 K, False
# 2) Edge case: 30 -> 86.0 F, 303.15 K, True
# 3) Error: -300 -> Error message


temp_c_input = input("Enter temperature in Celsius: ")
try:
    temp_c = float(temp_c_input)
    if temp_c < -273.15:
        print("Error: invalid input (below absolute zero)")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0
        print(f"Fahrenheit: {temp_f:.2f}")
        print(f"Kelvin: {temp_k:.2f}")
        print(f"High temperature: {is_high_temperature}")
except ValueError:
    print("Error: invalid input")


# Problem 2: Work hours and overtime payment
# Description: Calculates weekly pay, including overtime (1.5x) for hours > 40.
# Inputs:
# - hours_worked (int)
# - hourly_rate (float)
# Outputs:
# - Regular pay, Overtime pay, Total pay, Has overtime boolean.
# Validations:
# - hours >= 0, rate > 0.
# Test cases:
# 1) Normal: 45 hours, rate 10 - Reg:400, Over:75, Total:475, True
# 2) Edge case: 40 hours, rate 10 - Reg:400, Over:0, Total:400, False
 # 3) Error: -5 hours - "Error: invalid input"

hours_input = input("Enter hours worked: ")
rate_input = input("Enter hourly rate: ")
try:
    hours_worked = int(hours_input)
    hourly_rate = float(rate_input)
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40
        print(f"Regular pay: {regular_pay:.2f}")
        print(f"Overtime pay: {overtime_pay:.2f}")
        print(f"Total pay: {total_pay:.2f}")
        print(f"Has overtime: {has_overtime}")
except ValueError:
    print("Error: invalid input")

# Problem 3: Discount eligibility with booleans
# Description: Determines discount based on student status, senior status, or high purchase amount.
# Inputs:
# - purchase_total (float)
# - is_student_text ("YES"/"NO")
# - is_senior_text ("YES"/"NO")
# Outputs:
# - Eligible boolean, Final total.
# Validations:
# - purchase_total >= 0.
# - Text inputs must be YES or NO.
# Test cases:
# 1) Normal: 500, Student=YES -> Eligible: True, Total: 450.0
# 2) Edge case: 1000, Student=NO, Senior=NO -> Eligible: True, Total: 900.0
# 3) Error: -50 -> "Error: invalid input"

purchase_input = input("Enter purchase total: ")
student_input = input("Is student (YES/NO): ").strip().upper()
senior_input = input("Is senior (YES/NO): ").strip().upper()
try:
    purchase_total = float(purchase_input)
    if purchase_total < 0 or student_input not in ["YES", "NO"] or senior_input not in ["YES", "NO"]:
        print("Error: invalid input")
    else:
        is_student = student_input == "YES"
        is_senior = senior_input == "YES"
        discount_eligible = is_student or is_senior or purchase_total >= 1000.0
        final_total = purchase_total * 0.9 if discount_eligible else purchase_total
        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {final_total:.2f}")
except ValueError:
    print("Error: invalid input")
    
# Problem 4: Basic statistics of three integers
# Description: Calculates sum, avg, max, min and checks if all are even.
# Inputs:
# - n1, n2, n3 (int)
# Outputs:
# - Sum, Avg, Max, Min, All even boolean.
# Validations:
# - Must be integers.
# Test cases:
# 1) Normal: 2, 4, 6 - Sum:12, Avg:4.0, Even: True
# 2) Edge case: 1, 2, 3 - Sum:6, Avg:2.0, Even: False
# 3) Error: "a" - Handled by type check/try-except in real scenario.

try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print(f"Sum: {sum_value}")
    print(f"Average: {average_value:.2f}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")
except ValueError:
    print("Error: invalid input")
    

# Problem 5: Loan eligibility
# Description: Checks loan eligibility based on income, debt ratio, and credit score.
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
# Outputs:
# - Debt ratio, Eligible boolean.
# Validations:
# - income > 0, debt >= 0, score >= 0.
# Test cases:
# 1) Normal: Inc=9000, Debt=2000, Score=700 - Ratio=0.22, Eligible=True
# 2) Edge case: Inc=8000, Debt=3200 (Ratio 0.4), Score=650 - Eligible=True
# 3) Error: Inc=0 - "Error: invalid input"

income_input = input("Enter monthly income: ")
debt_input = input("Enter monthly debt: ")
score_input = input("Enter credit score: ")
try:
    monthly_income = float(income_input)
    monthly_debt = float(debt_input)
    credit_score = int(score_input)
    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = monthly_income >= 8000 and debt_ratio <= 0.4 and credit_score >= 650
        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {eligible}")
except ValueError:
    print("Error: invalid input")
    
# Problem 6: BMI Calculator
# Description: Calculates BMI and determines category booleans.
# Inputs:
# - weight_kg (float)
# - height_m (float)
# Outputs:
# - BMI, Underweight/Normal/Overweight booleans.
# Validations:
# - weight > 0, height > 0.
# Test cases:
# 1) Normal: 70kg, 1.75m - BMI=22.86 (Normal)
# 2) Edge case: 50kg, 1.80m - BMI=15.43 (Underweight)
# 3) Error: height=0 - "Error: invalid input"

weight_input = input("Enter weight in kg: ")
height_input = input("Enter height in meters: ")
try:
    weight_kg = float(weight_input)
    height_m = float(height_input)
    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m ** 2)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25
        is_overweight = bmi >= 25
        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")
except ValueError:
    print("Error: invalid input")
    
# GITHUB REPOSITORY: https://github.com/gladisalfaro2005-star/Projects