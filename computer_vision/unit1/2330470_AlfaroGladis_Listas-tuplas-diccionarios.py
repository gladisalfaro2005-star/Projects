# Problem 1: Shopping list basics
# Description: Manage a shopping list (create, add, search).
# Inputs: initial_items_text, new_item, search_item
# Outputs: Items list, Total, Found boolean
# Validations: Inputs not empty
# Test cases:
# 1) "apple,bread", "milk", "bread" -> Found: True
# 2) "", ... - Error

initial_items_text = input("Enter initial items: ")
new_item = input("Enter new item to add: ")
search_item = input("Enter item to search: ")

clean_text = initial_items_text.strip()
clean_new = new_item.strip()
clean_search = search_item.strip()

if clean_text:
    # Create list
    shopping_list = [item.strip().lower() for item in clean_text.split(',')]
    
    if clean_new:
        shopping_list.append(clean_new.lower())
        
    is_in_list = clean_search.lower() in shopping_list
    
    print(f"Items list: {shopping_list}")
    print(f"Total items: {len(shopping_list)}")
    print(f"Found item '{clean_search}': {is_in_list}")
else:
    print("Error: initial list cannot be empty")


# Problem 2: Points and distances (Tuples)
# Description: Calculate distance between two points.
# Inputs: x1, y1, x2, y2
# Outputs: Distance, Midpoint
# Validations: Numeric inputs
# Test cases:
# 1) 0,0, 3,4 - Dist: 5.0

print("Enter Point A coordinates:")
x1_str = input("x1: ")
y1_str = input("y1: ")
print("Enter Point B coordinates:")
x2_str = input("x2: ")
y2_str = input("y2: ")

try:
    x1 = float(x1_str)
    y1 = float(y1_str)
    x2 = float(x2_str)
    y2 = float(y2_str)
    
    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)
    
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance:.2f}")
    print(f"Midpoint: {midpoint}")
except ValueError:
    print("Error: invalid numeric input")

# Problem 3: Product catalog (Dictionary)
# Description: Get total price for a product.
# Inputs: product_name, quantity
# Outputs: Total price or error
# Validations: quantity > 0, product must exist
# Test cases:
# 1) "apple", 3 - Total
# 2) "car", 1 - Error

product_prices = {"apple": 10.0, "banana": 5.5, "orange": 8.0, "milk": 25.0}
print(f"Available: {list(product_prices.keys())}")

product_name = input("Enter product name: ")
quantity_str = input("Enter quantity: ")

search_key = product_name.strip().lower()

try:
    quantity = int(quantity_str)
    
    if quantity > 0:
        if search_key in product_prices:

            unit_price = product_prices[search_key]
            total = unit_price * quantity
            
            print(f"Unit price: {unit_price}")
            print(f"Total: {total}")
        else:
            print("Error: product not found")
    else:
        print("Error: quantity must be > 0")
except ValueError:
    print("Error: invalid quantity")

# Problem 4: Student grades (Dict + List)
# Description: Calculate average for a student.
# Inputs: student_name
# Outputs: Average, Passed status
# Validations: student must exist
# Test cases:
# 1) "Alice" -> Avg calculated

student_grades = {
    "alice": [90, 85, 95],
    "bob": [60, 65, 50],
    "charlie": [100, 98, 95]
}
print(f"Students: {list(student_grades.keys())}")

student_name = input("Enter student name: ")

search_student = student_name.strip().lower()

if search_student in student_grades:

    grades = student_grades[search_student]
    average = sum(grades) / len(grades)
    is_passed = average >= 70.0
    
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Passed: {is_passed}")
else:
    print("Error: student not found")

# Problem 5: Word frequency
# Description: Counts word frequency in a sentence.
# Inputs: sentence
# Outputs: Frequencies, most common word
# Validations: sentence not empty
# Test cases:
# 1) "Hello world hello" -> hello:2, world:1

sentence = input("Enter a sentence: ")

#  Convert
clean_sentence = sentence.strip().lower()

if clean_sentence:
    # Remove punctuation manually
    for char in ".,!?;:":
        clean_sentence = clean_sentence.replace(char, "")
        
    words_list = clean_sentence.split()
    freq_dict = {}
    
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
            
    # Find max
    most_common = max(freq_dict, key=freq_dict.get)
    
    print(f"Frequencies: {freq_dict}")
    print(f"Most common: {most_common}")
else:
    print("Error: sentence cannot be empty")


# Problem 6: Address book (CRUD)
# Description: Add, Search or Delete a contact.
# Inputs: action, name, (phone)
# Outputs: Action result
# Validations: Valid action, data present

phonebook = {"alice": "123-456"}

print("Actions: ADD, SEARCH, DELETE")
action_text = input("Enter action: ")
name = input("Enter name: ")

# Convert
action = action_text.strip().upper()
clean_name = name.strip().lower()
phone = "" # Default

if action == "ADD":
    phone = input("Enter phone: ").strip()

# Validate
valid_actions = ["ADD", "SEARCH", "DELETE"]

if action in valid_actions:
    if clean_name:
        # Calculate 
        if action == "ADD":
            if phone:
                phonebook[clean_name] = phone
                print(f"Saved: {clean_name}")
            else:
                print("Error: phone required")
                
        elif action == "SEARCH":
            if clean_name in phonebook:
                print(f"Phone: {phonebook[clean_name]}")
            else:
                print("Error: not found")
                
        elif action == "DELETE":
            if clean_name in phonebook:
                del phonebook[clean_name]
                print("Deleted")
            else:
                print("Error: not found")
    else:
        print("Error: name required")
else:
    print("Error: invalid action")
    
# GITHUB REPOSITORY: https://github.com/gladisalfaro2005-star/Projects