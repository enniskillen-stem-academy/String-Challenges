"""
Challenge 6: Default Password Creator

This program generates a default password for a new user based on their surname and today's date.

Instructions:
1. Run the program with the example input to see how it works.
2. Modify the `surname` variable and re-run the program to see different passwords.
3. Complete the TODO sections to expand and improve the program.
"""

# Starter Code
from datetime import datetime

def create_default_password(surname):
    """
    Generate a default password based on the surname and today's date.
    Args:
        surname (str): The surname of the user.
    Returns:
        str: Generated default password.
    """
    # Step 1: Get today's date.
    today = datetime.now()
    day_of_month = today.day

    # Step 2: Take the first three letters of the surname.
    first_three_letters = surname[:3].lower()

    # Step 3: Combine components to form the password.
    default_password = f"!{first_three_letters}{day_of_month}"

    return default_password

# Example Input
surname = "Smith"

# Generate and Print the Default Password
default_password = create_default_password(surname)
print("Surname:", surname)
print("Generated Password:", default_password)

# TODO 1: Test the program with different surnames and note the results in a comment.
# TODO 2: Modify the program to make the first letter of the password uppercase.
# Hint: Use the .capitalize() method.
# TODO 3: Write a new function that asks the user for their surname and generates the password dynamically.
