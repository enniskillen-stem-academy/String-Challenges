"""
Challenge 4: Text Obfuscator

This program censors bad words in a given text by replacing them with asterisks.

Instructions:
1. Run the program with the example input to see how it works.
2. Modify the `text` and `bad_words` variables to test it with different inputs.
3. Complete the TODO sections to expand the program's functionality.
"""

# Starter Code
def censor_bad_words(text, bad_words):
    """
    Replace bad words in the text with asterisks.
    Args:
        text (str): The input text.
        bad_words (list): A list of words to censor.
    Returns:
        str: The censored text.
    """
    # Step 1: Split the text into words.
    words = text.split()

    # Step 2: Check each word to see if it is in the list of bad words.
    censored_words = []
    for word in words:
        if word.lower() in bad_words:
            censored_words.append("*" * len(word))  # Replace the word with asterisks.
        else:
            censored_words.append(word)

    # Step 3: Join the words back into a single string.
    censored_text = " ".join(censored_words)

    return censored_text

# Example Input
text = "This is a bad example with some bad words."
bad_words = ["bad", "example"]

# Censor and Print the Result
censored_text = censor_bad_words(text, bad_words)
print("Original Text:", text)
print("Censored Text:", censored_text)

# TODO 1: Add more words to the bad_words list and test the program.
# TODO 2: Modify the program to handle words with different capitalizations (e.g., Bad, BAD).
# TODO 3: Write a new function that asks the user for bad words to add to the list dynamically.
