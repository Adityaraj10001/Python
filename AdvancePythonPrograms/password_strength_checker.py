password = input("Enter your password: ")

if len(password) < 8:
    print("Weak Password - Must be at least 8 characters")
elif password.isalnum():
    print("Weak Password - Must include special character")
elif not any(c.isupper() for c in password):
    print("Weak Password - Must include uppercase letter")
elif not any(c.islower() for c in password):
    print("Weak Password - Must include lowercase letter")
elif not any(c.isdigit() for c in password):
    print("Weak Password - Must include digit")
elif " " in password:
    print("Weak Password - Should not contain spaces")
else:
    print("Strong Password")