"""
Challenge 5: Aviation Phonetic Alphabet

This program converts a word or phrase into its phonetic alphabet equivalent.

Instructions:
1. Run the program with the example input to see how it works.
2. Change the `text` variable to test different words or phrases.
3. Complete the TODO sections to make the program more interactive and robust.
"""

# Starter Code
def to_phonetic_alphabet(text):
    """
    Convert a word or phrase into its phonetic alphabet equivalent.
    Args:
        text (str): Input text to convert.
    Returns:
        str: Phonetic alphabet representation of the input.
    """
    # Step 1: Define the phonetic alphabet mapping.
    phonetic_alphabet = {
        'a': "Alpha", 'b': "Bravo", 'c': "Charlie", 'd': "Delta", 'e': "Echo",
        'f': "Foxtrot", 'g': "Golf", 'h': "Hotel", 'i': "India", 'j': "Juliett",
        'k': "Kilo", 'l': "Lima", 'm': "Mike", 'n': "November", 'o': "Oscar",
        'p': "Papa", 'q': "Quebec", 'r': "Romeo", 's': "Sierra", 't': "Tango",
        'u': "Uniform", 'v': "Victor", 'w': "Whiskey", 'x': "X-ray", 'y': "Yankee",
        'z': "Zulu"
    }

    # Step 2: Convert each letter in the text to its phonetic equivalent.
    result = []
    for char in text.lower():
        if char in phonetic_alphabet:
            result.append(phonetic_alphabet[char])
        else:
            result.append(char)  # Keep non-alphabet characters as they are.

    return "-".join(result)

# Example Input
text = "G-TOYG"

# Convert and Print the Result
phonetic_result = to_phonetic_alphabet(text)
print("Original Text:", text)
print("Phonetic Alphabet:", phonetic_result)

# TODO 1: Try converting your name or a friend's name to the phonetic alphabet.
# TODO 2: Modify the program to handle uppercase letters directly (without converting to lowercase).
# TODO 3: Write a new function that allows users to input a word or phrase to convert.
