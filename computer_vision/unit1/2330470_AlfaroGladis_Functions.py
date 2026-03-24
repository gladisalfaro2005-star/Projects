# Problem 1: Rectangle area and perimeter
# Description: Calculates area and perimeter from user input.
# Inputs: width, height
# Outputs: Area, Perimeter
# Validations: width > 0, height > 0
# Test cases:
# 1) 5, 10 - Area: 50, Perimeter: 30
# 2) 0.1, 0.1 - Area: 0.01, Perimeter: 0.4
# 3) -5, 10 - Error

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width_str = input("Enter width: ")
height_str = input("Enter height: ")

try:
    width = float(width_str)
    height = float(height_str)

    if width > 0 and height > 0:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)
        
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    else:
        print("Error: invalid input (must be more than 0)")
except ValueError:
    print("Error: invalid input type")

# Problem 2: Grade classifier
# Description: Classifies a numeric score into a letter grade.
# Inputs: score
# Outputs: Category (A, B, C, D, F)
# Validations: 0 <= score <= 100
# Test cases:
# 1) 85 - B
# 2) 90 - A
# 3) 105 - Error

def classify_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

score_str = input("Enter score (0-100): ")

try:
    score = float(score_str)

    if 0 <= score <= 100:

        category = classify_grade(score)
        
        print(f"Score: {score}")
        print(f"Category: {category}")
    else:
        print("Error: invalid input (0-100)")
except ValueError:
    print("Error: invalid input type")


# Problem 3: List statistics function
# Description: Calculates min, max, and average from a comma-separated string.
# Inputs: numbers_text
# Outputs: min, max, average
# Validations: list not empty
# Test cases:
# 1) "10,20,30" - min:10, max:30, avg:20
# 2) "5" - min:5, max:5, avg:5
# 3) "" -Error

def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }


numbers_text = input("Enter numbers: ")

clean_text = numbers_text.strip()

if clean_text:
    try:
        str_list = clean_text.split(',')
        numbers_list = []
        for s in str_list:
            numbers_list.append(float(s.strip()))
        
        if len(numbers_list) > 0:

            stats = summarize_numbers(numbers_list)

            print(f"Min: {stats['min']}")
            print(f"Max: {stats['max']}")
            print(f"Average: {stats['average']}")
        else:
            print("Error: list is empty")
    except ValueError:
        print("Error: invalid input (non-numeric values)")
else:
    print("Error: input cannot be empty")


# Problem 4: Apply discount list
# Description: Applies a discount rate to a list of prices.
# Inputs: prices_text, discount_rate
# Outputs: Discounted prices list
# Validations: prices > 0, 0 <= rate <= 1
# Test cases:
# 1) "100,200", 0.1 -[90.0, 180.0]
# 2) "100", 0 - [100.0]
# 3) "100", 1.5 - Error

def apply_discount(prices_list, discount_rate):
    new_prices = []
    for price in prices_list:
        new_prices.append(price * (1 - discount_rate))
    return new_prices


prices_text = input("Enter prices: ")

rate_str = input("Enter discount rate (0.0 - 1.0): ")

try:
    discount_rate = float(rate_str)
    
    clean_prices = prices_text.strip()
    if clean_prices:
        str_prices = clean_prices.split(',')
        prices_list = []
        for p in str_prices:
            val = float(p.strip())
            prices_list.append(val)
        
        all_positive = all(p > 0 for p in prices_list)
        valid_rate = 0 <= discount_rate <= 1
        
        if all_positive and valid_rate and prices_list:
            discounted = apply_discount(prices_list, discount_rate)
            
            print(f"Original: {prices_list}")
            print(f"Discounted: {discounted}")
        else:
            print("Error: invalid input verify prices and rate")
    else:
        print("Error: empty prices")
except ValueError:
    print("Error: invalid numeric input")


# Problem 5: Greeting function
# Description: Greets user with optional title.
# Inputs: name, title
# Outputs: Greeting message
# Validations: Name not empty
# Test cases:
# 1) "Alice", "Dr." - Hello, Dr. Alice!
# 2) "Bob", "" - Hello, Bob!
# 3) "", "" - Error

def greet(name, title=""):
    if title:
        return f"Hello, {title} {name}!"
    return f"Hello, {name}!"

name = input("Enter name: ")
title = input("Enter title (optional, press Enter to skip): ")

clean_name = name.strip()
clean_title = title.strip()

if clean_name:
    message = greet(clean_name, clean_title)
    
    print(f"Greeting: {message}")
else:
    print("Error: invalid input, name is required")


# Problem 6: Factorial
# Description: Calculates factorial of n.
# Inputs: n
# Outputs: n!
# Validations: n integer, n >= 0
# Test cases:
# 1) 5 - 120
# 2) 0 - 1
# 3) -1 - Error

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n_str = input("Enter a number: ")

try:
    n = int(n_str)
    
    if n >= 0:
        result = factorial(n)
        print(f"Factorial of {n}: {result}")
    else:
        print("Error: invalid input.")
except ValueError:
    print("Error: invalid input, must be integer")
    
# GITHUB REPOSITORY: https://github.com/gladisalfaro2005-star/Projects