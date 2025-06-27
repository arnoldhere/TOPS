def top_n_values(d, n=3):
    # Sort dictionary items by value in descending order
    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    # Get the top n items
    return dict(sorted_items[:n])

my_dict = {'a': 50, 'b': 20, 'c': 70, 'd': 40, 'e': 90}
top_3 = top_n_values(my_dict, 3)
print("Top 3 highest values:", top_3)
