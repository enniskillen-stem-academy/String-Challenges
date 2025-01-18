"""
Challenge 2: Word Reverser

This program takes a sentence and reverses the order of its words.

Instructions:
1. Run the program with the example input to see how it works.
2. Modify the `sentence` variable with your own sentence.
3. Complete the TODO sections by writing your own code.
"""

# Starter Code
def reverse_words(sentence):
    """
    Reverse the words in the given sentence.
    Args:
        sentence (str): Input sentence to reverse.
    Returns:
        str: Sentence with words in reversed order.
    """
    # Step 1: Split the sentence into a list of words.
    words = sentence.split()

    # Step 2: Reverse the list of words.
    reversed_words = words[::-1]

    # Step 3: Join the reversed words into a single string.
    reversed_sentence = " ".join(reversed_words)

    return reversed_sentence

# Example Input
sentence = "Hello World! This is a test."

# Reverse and Print the Result
reversed_sentence = reverse_words(sentence)
print("Original Sentence:", sentence)
print("Reversed Sentence:", reversed_sentence)

# TODO 1: Try changing the sentence variable to your own sentence and see the result.
# TODO 2: Write a new function that reverses only the letters of each word while keeping the word order the same.
# Hint: Use a for loop to iterate over each word in the sentence and reverse the letters.
