"""
Challenge 8: Email Validator

This program checks if an email address is valid based on basic rules.

Instructions:
1. Run the program with the example email to see how it works.
2. Modify the `email` variable to test different email addresses.
3. Complete the TODO sections to add more validation rules.
"""

# Starter Code
def validate_email(email):
    """
    Check if an email address is valid.
    Args:
        email (str): The email address to validate.
    Returns:
        str: Validation result ('Valid' or 'Invalid').
    """
    # Step 1: Check for the '@' symbol.
    if "@" not in email:
        return "Invalid: Missing '@' symbol."

    # Step 2: Split the email into the local part and domain part.
    parts = email.split("@")
    if len(parts) != 2:
        return "Invalid: Incorrect '@' usage."

    local_part, domain_part = parts

    # Step 3: Check that the domain part contains at least one '.'
    if "." not in domain_part:
        return "Invalid: Domain must contain a '.'"

    return "Valid"

# Example Input
email = "example@domain.com"

# Validate and Print the Result
validation_result = validate_email(email)
print("Email Address:", email)
print("Validation Result:", validation_result)

# TODO 1: Test the program with different email addresses and note the results in a comment.
# TODO 2: Add a rule to check that the local part of the email is not empty.
# TODO 3: Write a new function that suggests a correction if the user misses '.com', '.org', etc.
