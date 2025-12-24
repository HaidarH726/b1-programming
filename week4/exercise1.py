# List of login attempts
login_attempts = [
    { "username": "alice", "status": "failed"},
    { "username": "alice", "status": "failed"},
    { "username": "alice", "status": "failed"},
    { "username": "bob", "status": "success"},
    { "username": "haidar","status": "failed"},
    { "username": "haidar", "status": "failed"},
    { "username": "haidar", "status": "success"},
    { "username": "jerry", "status": "success"}
]

failed_counts = {}

print('Checking login attempts')

for attempt in login_attempts:
    username = attempt["username"]
    status = attempt["status"]

    if status == "failed":
        print(f"{username} failed and can't login")
        failed_counts[username] = failed_counts.get(username, 0) + 1
    else:
        print(f"{username} login successful")

for user in failed_counts:
    if failed_counts[user] >= 3:
        print(f"alert {user} failed multiple times and cant login")

print("Security check completed")




