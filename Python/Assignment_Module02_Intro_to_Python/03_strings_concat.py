def swap_first_two_chars(str1, str2):
    # Swap first two characters of each string
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings must have at least 2 characters."
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    # Combine with a space
    return new_str1 + ' ' + new_str2

# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Swap and display
result = swap_first_two_chars(string1, string2)
print("Result:", result)
