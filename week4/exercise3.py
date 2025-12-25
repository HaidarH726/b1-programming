# List of passwords and their validity

passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123"]

min_length = 8
require_upper = True
require_lower = True
require_special = True
require_digits = True
compliant = 0
non_compliant = 0

print("Validating passwords...")

for password in passwords:
    print(f"checking : {password}")
    valid = True
    if len(password) < min_length:
        valid = False
        print("password is too short")
    if require_upper and not any(c.isupper() for c in password):
        valid = False
        print("password must contain at least one uppercase letter")
    if  require_lower and not any (c.islower() for c in password):
        valid = False
        print("Password must contain at least one lowercase letter")
    if  require_digits and not any (d.isdigit() for d in password):
        valid = False
        print(" password must contain a digit")
    if  require_special and not any (c.isalnum() for c in password):
        valid = False
        print(" password must contain at least one special character")
    elif valid:
        print("Password accepted")
        compliant += 1

    else:
        print("try again")
        non_compliant += 1


print(f"summary {compliant} compliant passwords and {non_compliant} non-compliant passwords")
