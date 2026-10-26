password = input("Enter a password: ")

errors = []

if len(password) < 8:
    errors.append("Password must contain at least 8 characters")

if not any(ch.isupper() for ch in password):
    errors.append("Include at least one uppercase letter")

if not any(ch.islower() for ch in password):
    errors.append("Include at least one lowercase letter")

if not any(ch.isdigit() for ch in password):
    errors.append("Include at least one digit")

if not any(not ch.isalnum() for ch in password):
    errors.append("Include at least one special character")

if "password" in password.lower():
    errors.append("Do not use the word 'password'")

if errors:
    print("Password is invalid")

    for error in errors:
        print("-", error)
else:
    print("Password is valid")