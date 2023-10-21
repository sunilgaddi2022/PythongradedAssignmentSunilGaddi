import re

print("Hello")
##First question : Create a Python script to check the password strength


def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for uppercase and lowercase letters
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return False

    # Check for at least one digit
    if not any(c.isdigit() for c in password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', password):
        return False

    return True

def main():
    password = input("Enter a password: ")
    is_strong = check_password_strength(password)

    if is_strong:
        print("Password is strong and meets all the criteria.")
    else:
        print("Password is weak and does not meet all the criteria. Please choose a stronger password.")

if __name__ == "__main__":
    main()