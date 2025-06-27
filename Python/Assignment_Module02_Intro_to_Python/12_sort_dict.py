from operator import itemgetter

def sort_dict_by_value(d, ascending=True):
    # itemgetter(1) gets the value from (key, value) pairs
    sorted_items = sorted(d.items(), key=itemgetter(1), reverse=not ascending)
    return dict(sorted_items)

my_dict = {'a': 3, 'b': 1, 'c': 2}

# Sort in ascending order
asc_sorted = sort_dict_by_value(my_dict, ascending=True)
print("Ascending:", asc_sorted)

# Sort in descending order
desc_sorted = sort_dict_by_value(my_dict, ascending=False)
print("Descending:", desc_sorted)
