def replace_not_poor_with_good(text):
    not_index = text.find('not')
    poor_index = text.find('poor')

    # Check if 'not' appears before 'poor'
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        # Replace 'not'...'poor' with 'good'
        return text[:not_index] + 'good' + text[poor_index + 4:]
    return text

# Get input from the user
sentence = input("Enter a sentence: ")

# Process and display the result
result = replace_not_poor_with_good(sentence)
print("Result:", result)
