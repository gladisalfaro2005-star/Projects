# Problem 1: Sum of integers
# Description: Sum 1..n and even numbers.
# Inputs: n
# Outputs: Sum, Even Sum
# Validations: n >= 1

n_str = input("Enter n: ")

try:
    n = int(n_str)
    
    if n >= 1:
        total_sum = 0
        even_sum = 0
        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        
        print(f"Sum 1..{n}: {total_sum}")
        print(f"Even sum: {even_sum}")
    else:
        print("Error: invalid input (must be >= 1)")
except ValueError:
    print("Error: invalid input type")


# Problem 2: Multiplication table
# Description: Print table for base up to m.
# Inputs: base, m
# Outputs: Table lines
# Validations: m >= 1

base_str = input("Enter base: ")
m_str = input("Enter limit m: ")

try:
    base = int(base_str)
    m = int(m_str)
    
    if m >= 1:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
    else:
        print("Error: m must be >= 1")
except ValueError:
    print("Error: invalid input")


# Problem 3: Average with sentinel
# Description: Read numbers until -1 is entered.
# Inputs: number (repeated)
# Outputs: Count, Average
# Validations: number >= 0

total = 0.0
count = 0
SENTINEL = -1.0

while True:
    num_str = input("Enter number (-1 to stop): ")
    
    try:
        val = float(num_str)
     
        if val == SENTINEL:
            break
            
        if val >= 0:
            total += val
            count += 1
        else:
            print("Error: invalid input")
    except ValueError:
        print("Error: invalid input")

if count > 0:
    print(f"Count: {count}")
    print(f"Average: {total / count}")
else:
    print("Error, no data")


# Problem 4: Password attempts
# Description: Max 3 attempts to guess password.
# Inputs: user_password
# Outputs: Success/Lock

SECRET = "admin123"
MAX_ATTEMPTS = 3
attempts = 0
success = False

while attempts < MAX_ATTEMPTS:
    user_password = input(f"Attempt {attempts+1}: Enter password: ")
    
    attempts += 1
    if user_password == SECRET:
        success = True
        break
    else:
        print("Wrong password")

if success:
    print("Login success")
else:
    print("Account locked")


# Problem 5: Menu
# Description: Simple menu loop.
# Inputs: option
# Outputs: Action result

counter = 0
option = -1

while option != 0:
    print("\n1:Greet, 2:Show, 3:Inc, 0:Exit")

    opt_str = input("Select option: ")
    
    try:
        option = int(opt_str)
        
        if option == 1:
            print("Hello!")
        elif option == 2:
            print(f"Counter: {counter}")
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
        else:
            print("Error: invalid option")
            
    except ValueError:
        print("Error: invalid option")


# Problem 6: Pattern
# Description: Print triangle of stars.
# Inputs: n
# Outputs: Stars
# Validations: n >= 1

n_str = input("Enter rows n: ")

try:
    n = int(n_str)
    
    if n >= 1:
        for i in range(1, n + 1):
            print("*" * i)
    else:
        print("Error: n must be >= 1")
except ValueError:
    print("Error: invalid option")
    
# GITHUB REPOSITORY: https://github.com/gladisalfaro2005-star/Projects