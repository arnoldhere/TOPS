# Counting the frequencies in a list using a dictionary in Python.

l = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]

print("The list is : \n " , l)

def count_freq_nums(l):
    num_count = {}
    for n in l:
        if n in num_count:
            num_count[n] +=1
        else:
            num_count[n]=1
    return num_count

print("\n======================Frequencies of numbers=======================\n") 

freqs = count_freq_nums(l)

for num, count in freqs.items():
    print(f"{num}: {count}")