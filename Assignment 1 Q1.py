password = input("Please enter your password:")
has_digit = False
has_upper = False
for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True
if len(password) < 8:
        print("password must be at least 8 characters long")
if not has_digit:
        print("password must contain at least one digit")
if not has_upper:
        print("password must contain at least one uppercase letter")
if len(password) >= 8 and has_digit and has_upper:
    print("password is valid")
else:
    print("password is invalid")