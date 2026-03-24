# Problem 1: Full name formatter (name + initials)
# Description: Asks the user for their full name and formats it correctly.
# Input: full_name (string)
# Output: Formatted name or error message
# Rules:
# - Must contain at least two words
# - No numbers allowed
# - Extra spaces removed
# Test cases:
# 1) "JuAn Perez" - Formatted name: Juan Perez
# 2) "  maria   lopez  "- Formatted name: Maria Lopez
# 3) "Juan" or "   "- Error. Please enter your full name

full_name = input("Enter full name: ")

clean_name = full_name.strip() # to remove spaces

if clean_name == "": # if the user dosent writes anything
       print("Error. Please enter your full name")

elif len(clean_name.split()) < 2:
    print("Name is too short")

else: 
    name_parts = clean_name.split() # split words

    format_name = " ".join(name_parts).title() # capital letter

    initials = "" # save initials
    for part in name_parts: # for each word in name oarts
          initials += part[0].upper() + "." # join initials and dot

    print(f"Formatted name: {format_name}")
    print(f"Initials: {initials}")

# Problem 2: Simple email validator (structure + domain)
# Description: Checks if an email has a valid format.
# Input: email_txt (string)
# Output: Valid email or error message
# Rules:
# - Must contain one @
# - Domain must contain a dot
# - Dot cannot be first or last in domain
# Test cases:
# 1) "USER@GMAIL.COM" or "user@gmail.com" or "a@b.co" - Valid email. True
# 2) "  " - Error. empty email
# 3) "user@gmailcom" or "user@.com" - Valid email: False

email_txt = input("Enter email: ")

clean_email = email_txt.strip().lower()  # clean spaces, all in lower case

at_position = clean_email.find("@")

if clean_email == "":
    print("Error: empty email")

elif at_position == -1:  # there is not @
    print("Valid email: False")

elif clean_email[at_position + 1:].find("@") != -1:  # more than one @
    print("Valid email: False")

else:
    user_part = clean_email[:at_position]
    domain_part = clean_email[at_position + 1:]

    if user_part == "":
        print("Valid email: False")

    elif "." not in domain_part:
        print("Valid email: False")

    elif domain_part[0] == "." or domain_part[-1] == ".":
        print("Valid email: False")

    else:
        print("Valid email: True")
        print(f"Domain: {domain_part}")

# Problem 3. Palindrome checker (ignoring spaces and case)
# Description: Checks if a word or phrase is a palindrome.
# Input: text_input (string)
# Output: True or False
# Rules:
# - Ignore spaces
# - Ignore upper/lower case
# Test cases:
# 1) "ana" - True
# 2) "AnA" - True
# 3) "anita lava la tina" - True
# 4) "hola" - False

phrase = input("Enter a phrase: ")
    
clean_phrase = phrase.replace(" ", "").lower() # replace deletes spaces and lower makes everithing to lower case

reversed_phrase = clean_phrase[::-1] # this function helps to reverse the string

if clean_phrase == "":
        print("Error. Please enter a phrase")    
        
elif clean_phrase == reversed_phrase:
        print("Is palindrome: True")
        
else:
        print("Is palindrome: False")
        

    
normalized_phrase = clean_phrase.lower().replace(" ", "")
print(f"Normalized phrase: {normalized_phrase}")


# problem 4: Sentence word statistics (lengths and first/last word)
# Description: Given a sentence, analyzes word statistics.
# Steps:
# - Remove extra spaces at beginning and end
# - Split sentence into words
# Outputs:
# - Total number of words
# - First word
# - Last word
# - Shortest word
# - Longest word
# Input: sentence (string)
# Validations:
# - Sentence must not be empty after strip()
# - Must contain at least one valid word
# Key operations: strip(), split(), len(), loop through words

sentence = input("Enter a sentence: ")

clean_sentence = sentence.strip() # to remove spaces

spare = clean_sentence.split() # to separate words

if len(spare) == 0:
    print("Error. Please enter a sentence")
    
else:
    word_lengths = [len(word) for word in spare] # list comprehension to get the length of each word
    
    word_count = len(spare) # count the number of wordds
    first_word = spare[0]
    last_word = spare[-1]
    shortest_word = min(spare, key=len) # key len counts the lenght of the word and min returns the shortest
    longest_word = max(spare, key=len)
    
    print(f'Word count: {word_count}')
    print(f"Word lengths: {word_lengths}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")

#  Problem 5: Password strength classifier
# Description: Evaluates password strength.
# Input: password_input (string)
# Output: Weak, Medium or Strong password
# Rules:
# - Weak: length < 8
# - Medium: length >= 8 and letters + digits
# - Strong: length >= 10, upper, lower and digits
# Test cases:
# 1) "abc12345" - Medium password
# 2) "Abc1234567" - Strong password
# 3) "abcdefgh" - Weak password
# 4) "12345" - Weak password

password_input = input("Please enter your password:")

spare_password = password_input.strip() # we eliminate spaces

if spare_password == "":
    print("Error: empty password")
    
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for c in spare_password: # c indicates each character in the password
        if c.isupper():     # isupper checks if the character is uppercase
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif not c.isalnum():
            has_symbol = True

    if len(spare_password) < 8:
        print("Password strength: weak")

    elif len(spare_password) >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")

    elif len(spare_password) >= 8 and ((has_upper and has_lower) or has_digit):
        print("Password strength: medium")

    else:
        print("Password strength: weak")
        
# Problem 6: Product label formatter (fixed-width text)
# Description: Formats a product label with fixed width.
# Format: Product: <NAME> | Price: $<PRICE>
# The final label must have exactly 30 characters.
# Rules:
# - If shorter than 30 characters, pad with spaces at the end
# - If longer than 30 characters, cut to 30 characters
# Inputs:
# - product_name (string)
# - price_value (number or string)
# Output:
# - Label with exactly 30 characters (can be shown in quotes)
# Validations:
# - product_name must not be empty after strip()
# - price_value must be a positive number
# Key operations: f-strings, len(), slicing [:30], space padding


product_name = input("Enter product name: ")

product_value = input("Enter product price: ")

clean_product = product_name.strip()

if clean_product == "":
    print("Error. Please enter a product name")
    
elif not product_value.replace(".", "", 1).isdigit(): # this checks if the price is a valid number 
    print("Error. Please enter a valid price")
    
label = f"Product: {clean_product} | Price: ${product_value}"

if len(label) > 30:
    label = label[:30] # this cuts the label to 30 characters
    
else:
    label = label + " " * (30 - len(label)) # this adds spaces to the end of the label to make it 30 characters long
    
print(f'Label: "{label}"')
print(f"Length: {len(label)}")

# GITHUB REPOSITORY: https://github.com/gladisalfaro2005-star/Projects
