def add_suffix(word):
    if len(word) < 3:
        return "Enter valid length of string"
    elif word.endswith("ing"):
        return word + "ly"
    else:
        return word + "ing"

# Get input from the user
user_input = input("Enter a word: ")

# Process and display the result
result = add_suffix(user_input)
print("Result:", result)
