# ●	Validate a password based on these conditions: 
# o	Minimum 8 characters 
# o	At least one uppercase letter 
# o	One lowercase letter 
# o	One digit 
# o	One special character

password=input("Enter a password: ")
if len(password)<8 :
    print("password is invalid")
else:
    has_upper=False
    has_lower=False
    has_digit=False
    has_special=False
    special_characters="!@#$%^&*()-+"
    
    for i in password:
        if i.isupper():
            has_upper=True
        if i.islower():
            has_lower=True
        if i.isdigit():
            has_digit=True
        if i in special_characters:
            has_special=True
    
    if has_upper and has_lower and has_digit and has_special:
        print("password is valid")
    else:
        print("password is invalid")
        