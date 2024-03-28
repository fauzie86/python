name = input("Enter your name:")
email = input("Enter your email:")

k, j, d = 0, 0, 0

# Email validation
if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:  #abc@gmail.co
            if email[-4] == "." or email[-3] == ".":  # abc@gmail.com
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:  # simplified the code
                        continue
                else:
                    d = 1
                if k == 1 or j == 1 or d == 1:
                    print("wrong email format")
                else:
                    print("correct email format")
            else:
                print("Wrong email format: missing or misplaced the dot")
        else:
            print("Wrong email format: incorrect number of @ symbol")
    else:
        print("Wrong email format: email must start with a letter")
else:
    print("Wrong email format: length should be at least 6 characters")

# Name validation
if not name.isalpha():
    print("Invalid name: Name should only contain alphabetic characters")
else:
    print("Valid name")

# Additional condition to check if both email and name are valid
if (k == 0 and j == 0 and d == 0) and name.isalpha():
    print("Both email and name are valid!")




