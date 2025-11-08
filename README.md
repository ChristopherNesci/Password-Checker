# Password-Checker

Simple Password Validator

A Python-based password strength checker that validates passwords against security criteria and checks them against common password lists.

## Features:
- Validates password strength based on security best practices
- Checks passwords against leaked password lists (provided by you)
- Continuous input mode, allows multiple password checks in one session
- Supports multiple password list files

## Password Criteria

Checks if your password meets the following criteria:
- Minimum length of 8 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character, eg !@#$%^&*()


If password passes the above checks, then it is checked again a common password lists.

## Installation

1. Clone repository
```bash
git clone https://github.com/ChristopherNesci/Password-Validator.git
cd Password-Validator
```

2. Ensure you have Python 3 installed:
```bash
python3 --version
```
## Usage

Run the program:

```bash
python3 password_checker.py
```

Enter a password when prompted and the program will:

1. Check if your password meets security criteria
2. Seach for you password in common password lists
3. Give you feedback on password strength and what to add to meet criteria

Type 'quit' to exit the program

## Password lists

Place passwords lists files ('txt' format) into the 'password_lists/' directory
Password Checker will check all txt files in this folder

Resources for passwords lists:
https://github.com/danielmiessler/SecLists
https://weakpass.com/

## Example
```
       ___                                    _     ___ _               _             
      / _ \__ _ ___ _____      _____  _ __ __| |   / __\ |__   ___  ___| | _____ _ __ 
     / /_)/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  / /  | '_ \ / _ \/ __| |/ / _ \ '__|
    / ___/ (_| \__ \__  \ V  V / (_) | | | (_| | / /___| | | |  __/ (__|   <  __/ |   
    \/    \__,_|___/___/ \_/\_/ \___/|_|  \__,_| \____/|_| |_|\___|\___|_|\_\___|_|   
    
        Validate your password!
        
        Password should meet the following criteria:
        - Minimum length of 8 characters
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one digit
        - Contains at least one special character, eg !@#$%^&*()"

        Type 'quit' to exit

        Enter Password: hello

        - Password is too short!
        - You need at least 1 upper case letter!
        - You need at least 1 digit!
        - You need at least 1 special character!

        Enter Password: Password123!
        
        'Password123!' found in the following lists:
        rockyou.txt

        Enter Password: My3picP@ssw0dRu7z 
        
        'My3picP@ssw0dRu7z' not found in any list and meets all criteria  
       ```
        
## Security Note

This tool is for education purposes only. Dont actuall put real passwords youre currently using into any password checking tool unless you trust it.
