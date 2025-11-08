import os

def check_password():
    while True:
        print(
        "Passwork Validator\n"
        " Password should meet the following criteria:\n" 
        " - Minimum length of 8 characters.\n"
        " - Contains at least one uppercase letter.\n"
        " - Contains at least one lowercase letter.\n"
        " - Contains at least one digit.\n"
        " - Contains at least one special character, eg !@#$%^&*().\n"
        )

        print("Type 'quit' to exit\n")
                                             

        user_input = input("Enter Password: ")

        if user_input.lower() == 'quit':
            print("Goodbye")
            break

        if len(user_input) < 8:
            print("Password is too short!\n")
        
        if not any(letter.isupper() for letter in user_input):
            print("You need at least 1 upper case letter!")
        
        if not any(letter.islower() for letter in user_input):
            print("You need at least 1 lower case letter!")

        if not any(letter.isdigit() for letter in user_input):
            print("You need at least 1 digit!")
        
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

        if not any(letter in user_input for letter in special_chars):
            print("You need at least 1 special character!")

        found_in = []

        for filename in os.listdir("password_lists"):
            filepath = os.path.join("password_lists", filename)
        
            if not os.path.isfile(filepath):
                continue

            with open(filepath, encoding='utf-8', errors='ignore') as f:
                file_contents = f.read()
                if user_input in file_contents:
                    found_in.append(filename)
    
        if found_in:
            print(f"'{user_input}' found in the following lists:\n")
            print(*found_in, sep=', ')
        else:
            print(f"'{user_input}' not found in any list")
        
        print()

check_password()