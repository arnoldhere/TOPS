def count_word_occurrences(sentence):
    # Convert to lowercase
    sentence = sentence.lower()
    # Split into words
    words = sentence.split()
    # Count occurrences
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Input from user
sentence = input("Enter a sentence: ")

# Count words
occurrences = count_word_occurrences(sentence)
# Display results
print("Word occurrences:")
for word, count in occurrences.items():
    print(f"{word}: {count}")