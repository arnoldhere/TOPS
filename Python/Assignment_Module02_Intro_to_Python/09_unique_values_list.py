def get_unique_values(numbers):
    unique_values = []
    for num in numbers:
        if num not in unique_values:
            unique_values.append(num)
    return unique_values

numbers = [1, 2, 3, 4, 2, 5, 1, 6, 3]
result = get_unique_values(numbers)
print(f"Unique values: {result}")
