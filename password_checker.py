import os


def check_password():
    while True:
        art = """
    ____                                          __   _    __      ___     __      __              
   / __ \____ ____________      ______  _________/ /  | |  / /___ _/ (_)___/ /___ _/ /_____  _____        
  / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  /   | | / / __ `/ / / __  / __ `/ __/ __ \/ ___/ 
 / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /    | |/ / /_/ / / / /_/ / /_/ / /_/ /_/ / /    
/_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/     |___/\__,_/_/_/\__,_/\__,_/\__/\____/_/     
                                                                                       
        """
        print(art)
        print(
            "Validate your password!\n"
            "\n"
            " Password should meet the following criteria:\n"
            " - Minimum length of 8 characters.\n"
            " - Contains at least one uppercase letter.\n"
            " - Contains at least one lowercase letter.\n"
            " - Contains at least one digit.\n"
            " - Contains at least one special character, eg !@#$%^&*().\n"
        )

        print("Type 'quit' to exit\n")

        user_input = input("Enter Password: ")

        SPECIAL_CHARS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
        if user_input.lower() == "quit":
            print("Goodbye")
            break

        is_valid = True

        if len(user_input) < 8:
            print("Password is too short!")
            is_valid = False

        if not any(letter.isupper() for letter in user_input):
            print("You need at least 1 upper case letter!")
            is_valid = False

        if not any(letter.islower() for letter in user_input):
            print("You need at least 1 lower case letter!")
            is_valid = False

        if not any(letter.isdigit() for letter in user_input):
            print("You need at least 1 digit!")
            is_valid = False

        if not any(letter in user_input for letter in SPECIAL_CHARS):
            print("You need at least 1 special character!")
            is_valid = False

        if not is_valid:
            print()
            continue

        found_in = []

        for filename in os.listdir("password_lists"):
            filepath = os.path.join("password_lists", filename)

            if not os.path.isfile(filepath):
                continue

            with open(filepath, encoding="utf-8", errors="ignore") as f:
                file_contents = f.read()
                if user_input in file_contents:
                    found_in.append(filename)

        if found_in:
            print(f"'{user_input}' found in the following lists:\n")
            print(*found_in, sep=", ")
        else:
            print(f"'{user_input}' not found in any list and meets all criteria")

        print()


if __name__ == "__main__":
    check_password()
