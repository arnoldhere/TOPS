# Write a Python program to count occurrences of a substring in a string

def count_substring_occurrences(main_string, substring):
    return main_string.count(substring)

# Taking input from the user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

count = count_substring_occurrences(main_string, substring)
print(f"The substring '{substring}' occurs {count} time(s) in the given string.")
