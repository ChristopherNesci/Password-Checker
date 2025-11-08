import os


def check_password():
    art = """
       ___                                    _     ___ _               _             
      / _ \__ _ ___ _____      _____  _ __ __| |   / __\ |__   ___  ___| | _____ _ __ 
     / /_)/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  / /  | '_ \ / _ \/ __| |/ / _ \ '__|
    / ___/ (_| \__ \__  \ V  V / (_) | | | (_| | / /___| | | |  __/ (__|   <  __/ |   
    \/    \__,_|___/___/ \_/\_/ \___/|_|  \__,_| \____/|_| |_|\___|\___|_|\_\___|_|   
                                                                                       
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
    while True:
        user_input = input("Enter Password: ")

        SPECIAL_CHARS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
        if user_input.lower() == "quit":
            print("Goodbye")
            break

        is_valid = True

        if len(user_input) < 8:
            print("- Password is too short!")
            is_valid = False

        if not any(letter.isupper() for letter in user_input):
            print("- You need at least 1 upper case letter!")
            is_valid = False

        if not any(letter.islower() for letter in user_input):
            print("- You need at least 1 lower case letter!")
            is_valid = False

        if not any(letter.isdigit() for letter in user_input):
            print("- You need at least 1 digit!")
            is_valid = False

        if not any(letter in user_input for letter in SPECIAL_CHARS):
            print("- You need at least 1 special character!")
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
