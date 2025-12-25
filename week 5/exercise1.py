# Password validation tool
password = input("enter your password:")
def check_password(password):
    if password == "":
        return True
    if len(password) > 8:
        return True
    if password == "":
        return True
    if password.isdigit():
        return True
    if password.islower():
        return True
    if password.isupper():
        return True
    if password.isspecial():
        return True
    else:
        return False
