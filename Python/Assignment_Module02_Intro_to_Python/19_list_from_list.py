def get_unique_elements(input_list):
    unique_list = []
    seen = set()
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

l = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]

print("Unique list \n " , get_unique_elements(l))