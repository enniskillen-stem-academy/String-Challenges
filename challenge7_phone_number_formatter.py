"""
Challenge 7: Phone Number Formatter

This program checks if a phone number is valid and formats it into the international format: +44 (0) 7000 000000.

Instructions:
1. Run the program with the example input to see how it works.
2. Modify the `phone_number` variable to test different inputs.
3. Complete the TODO sections to improve the program and add new features.
"""

# Starter Code
def format_phone_number(phone_number):
    """
    Validate and format a UK phone number into the international format.
    Args:
        phone_number (str): The phone number to validate and format.
    Returns:
        str: Formatted phone number, or an error message if invalid.
    """
    # Step 1: Remove any spaces or dashes from the input.
    cleaned_number = phone_number.replace(" ", "").replace("-", "")

    # Step 2: Check if the number starts with '07' and is 11 digits long.
    if cleaned_number.startswith("07") and len(cleaned_number) == 11:
        # Step 3: Format the number.
        formatted_number = f"+44 (0) {cleaned_number[1:4]} {cleaned_number[4:7]} {cleaned_number[7:]}"
        return formatted_number
    else:
        return "Invalid phone number. Please ensure it starts with '07' and is 11 digits long."

# Example Input
phone_number = "07000 123456"

# Format and Print the Result
formatted_number = format_phone_number(phone_number)
print("Original Phone Number:", phone_number)
print("Formatted Phone Number:", formatted_number)

# TODO 1: Test the program with different phone numbers and note the results in a comment.
# TODO 2: Modify the program to accept numbers starting with '+447' as valid.
# TODO 3: Write a new function to handle international numbers from other countries.
