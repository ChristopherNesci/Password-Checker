import os

def check_input():
    user_input = input("Enter Password: ")
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
        print(f"'{user_input}' found in: {', '.join(found_in)}")
    else:
        print(f"'{user_input}' not found in any list")

check_input()