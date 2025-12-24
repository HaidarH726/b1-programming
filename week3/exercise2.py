max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")

    if len(password) >= 8 and any(char.isdigit() for char in password):
        print("Password accepted")
        break   # exit loop if password is valid
    else:
        attempts += 1
        print(f"Wrong password. Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Error: account locked due to too many failed attempts")
