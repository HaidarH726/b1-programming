# Password validation tool

import string
import random
# PART A
def check_min_length(password, min_length=8):
    return len(password) >= min_length
def has_uppercase(password):
    return any(char.isupper() for char in password)
def has_lowercase(password):
    return any(char.islower() for char in password)
def has_digit(password):
   return any(char.isdigit() for char in password)
def has_special(password):
    return any(char in string.punctuation for char in password)


# PART B
def validate_password(password):
        results = {
            "min_length": check_min_length(password),
            "uppercase": has_uppercase(password),
            "lowercase": has_lowercase(password),
            "digits": has_digit(password),
            "special": has_special(password)
        }

        results["is_valid"] = all(results.values())
        return results
#PART C
def main():
    password = input("Enter your password: ")
    result = validate_password(password)

    print("\nPassword check results:")
    print("Minimum length:", "Met" if result["min_length"] else "Not met")
    print("Has uppercase:", "Met" if result["uppercase"] else "Not met")
    print("Has lowercase:", "Met" if result["lowercase"] else "Not met")
    print("Has digit:", "Met" if result["digits"] else "Not met")
    print("Has special character:", "Met" if result["special"] else "Not met")

    if result["is_valid"]:
        print("\nYour password is STRONG 💪")
    else:
        print("\nYour password is WEAK ❌")


if __name__ == "__main__":
    main()



