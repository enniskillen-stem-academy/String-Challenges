"""
Challenge 3: Password Strength Checker

This program checks how strong a password is and tells you if it's Weak, Good, or Strong.

Instructions:
1. Run the program and type in a password when asked.
2. Change the rules in the `check_password_strength` function to experiment with different checks.
3. Complete the TODO sections by writing your own code to add features.
"""

# Starter Code
def check_password_strength(password):
    """
    Check how strong a password is.
    Args:
        password (str): The password to check.
    Returns:
        str: Strength of the password ('Weak', 'Good', 'Strong').
    """
    # Step 1: Define simple rules for password strength.
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in "!@#$%^&*()-_+=<>?/" for char in password)
    is_long_enough = len(password) >= 8

    # Step 2: Check the rules and decide the strength.
    if is_long_enough and has_number and has_symbol:
        return "Strong"
    elif is_long_enough and (has_number or has_symbol):
        return "Good"
    else:
        return "Weak"

# Example Input
password = input("Type a password to see how strong it is: ")

# Check Password Strength
strength = check_password_strength(password)
print(f"Your password is: {strength}")

# TODO 1: Try creating passwords that are Weak, Good, and Strong. Write them down in a comment.
# TODO 2: Add a rule to check if the password has at least one uppercase letter.
# Hint: Use the .isupper() method for this.
# TODO 3: Write a new function that gives tips on how to make a password stronger.
