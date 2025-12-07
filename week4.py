# List of login attempts

login_attempts = [
    { "username": "alice", "status": "failed"},
    { "username": "bob", "status": "success"},
    { "username": "haidar","status": "failed"},
    { "username": "jerry", "status": "success"}]

for attempt in login_attempts:
    username = attempt ["username"]
    status = attempt ["status"]
    if status == "failed":
        print(f"{username} failed and can't login")
    elif status == "failed">=3:
        print(f"alert {username} failed 3 or more times")
else:
    print(f" {username} login successful")



