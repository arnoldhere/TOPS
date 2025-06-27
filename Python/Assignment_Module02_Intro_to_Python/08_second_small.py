def second_smallest(numbers):
    # Remove duplicates to ensure there are at least two distinct numbers
    unique_numbers = list(set(numbers))    
    unique_numbers.sort()
    if len(unique_numbers) >= 2:
        return unique_numbers[1]  # Return the second smallest number
    else:
        return None  # Return None if there is no second smallest number

numbers = [7, 2, 3, 1, 0, 5]
result = second_smallest(numbers)
if result is not None:
    print(f"The second smallest number is: {result}")
else:
    print("There is no second smallest number.")
