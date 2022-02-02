users = {}
command = input()

while not command == "Statistics":
    data = command.split("->")
    action, username = data[0], data[1]
    if action == "Add":
        if username not in users:
            users[username] = []
        else:
            print(f"{username} is already registered")
    elif action == "Send":
        email = data[2]
        if username in users:
            users[username].append(email)
    elif action == "Delete":
        if username in users:
            users.pop(username)
        else:
            print(f"{username} not found!")

    command = input()

sorted_users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))
users_count = len(users)

print(f"Users count: {users_count}")

for user, mails in sorted_users.items():
    print(user)
    for mail in mails:
        print(f" - {mail}")
