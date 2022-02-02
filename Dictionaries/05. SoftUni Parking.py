
number_of_commands = int(input())
users = {}

for plates in range(number_of_commands):
    command = input().split(" ")

    if command[0] == "register":
        user = command[1]
        plate = command[2]
        if user not in users:
            users[user] = plate
            print(f"{user} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")

    elif command[0] == "unregister":
        user = command[1]
        if user in users:
            del users[user]
            print(f"{user} unregistered successfully")
        else:
            print(f"ERROR: user {user} not found")

for name, plate in users.items():
    print(f"{name} => {plate}")
