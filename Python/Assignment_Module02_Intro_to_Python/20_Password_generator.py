import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password

    def get_details(self):
        return (self.user_id, self.name, self.password)

def generate_password(input_words):
    try:
        if not input_words or not isinstance(input_words, list):
            raise ValueError("Input must be a non-empty list of words.")

        # Select 2 or 3 random words
        selected_words = random.sample(input_words, min(3, len(input_words)))
        
        # Capitalize random letters in words
        transformed_words = []
        for word in selected_words:
            if len(word) > 1:
                index = random.randrange(len(word))
                word = word[:index] + word[index].upper() + word[index + 1:] 
            transformed_words.append(word)
        
        # Join words and add random digits and special characters
        base_password = ''.join(transformed_words)
        digits = ''.join(random.choices(string.digits, k=2))
        specials = ''.join(random.choices("!@#$%^&*()", k=2))

        full_password = base_password + digits + specials
        # Ensure password is at least 8 characters
        while len(full_password) < 8:
            full_password += random.choice(string.ascii_letters + string.digits + "!@#$%^&*()")
        return full_password

    except Exception as e:
        print("Error generating password:", e)
        return None

def main():
    try:
        print("=== Password Generator ===")
        user_id = input("Enter User ID: ")
        name = input("Enter your Name: ")
        words_input = input("Enter some words (space separated): ")
        word_list = words_input.strip().split()

        password = generate_password(word_list)

        if password:
            user = User(user_id, name, password)
            print("\nUser created successfully!")
            print("User Details :", user.get_details())
        else:
            print("Failed to create user due to password error.")

    except Exception as e:
        print("An unexpected error occurred:", e)

main()