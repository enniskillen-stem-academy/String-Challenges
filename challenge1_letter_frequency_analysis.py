"""
Challenge 1: Letter Frequency Analysis

This program will analyse the frequency of letters in a given text and
output the top five most frequently occurring letters.

Instructions:
1. Run the code to see how it works.
2. Modify the `text` variable with your own input to test it.
3. Follow the comments in the code to understand how it operates.
4. Complete the TODO sections to enhance functionality.
"""

# Starter Code
def analyse_letter_frequency(text):
    """
    analyse the frequency of letters (how many times they appear) in the given text.
    Args:
        text (str): Input text to analyse.
    Returns:
        list: Top five most frequent letters with their counts.
    """
    from collections import Counter

    # Step 1: Clean the text by removing spaces and converting to lowercase.
    cleaned_text = text.replace(" ", "").lower()

    # Step 2: Count the frequency of each letter.
    letter_counts = Counter(cleaned_text)

    # Step 3: Get the top five most frequent letters.
    top_five = letter_counts.most_common(5)

    return top_five

# Example Input
text = "This is a simple example to analyse letter frequency."

# analyse and Print Results
results = analyse_letter_frequency(text)
print("Top 5 most frequent letters:")
for letter, count in results:
    print(f"'{letter}' appears {count} times.")

# TODO: Enhance the program to ignore non-alphabetic characters (e.g., punctuation).
