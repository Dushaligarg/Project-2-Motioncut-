# Word Counter Program

def count_words(text):
    """
    Function to count the number of words in the given text.
    A word is defined as any sequence of characters separated by whitespace.
    """
    words = text.split()  # Split the text into words based on spaces
    return len(words)  # Return the count of words

# User Input: Prompt the user to enter a sentence or paragraph
user_input = input("Enter a sentence or paragraph: ").strip()

# Error Handling: Check if input is empty
if not user_input:
    print("Error: No input provided. Please enter some text.")
else:
    # Word Counting Logic: Count the words in the input
    word_count = count_words(user_input)
    
    # Output Display: Print the word count to the console
    print(f"Word Count: {word_count}")
