age = float(input())
gender = input()


if gender == "f":
    if age >= 16:
        print("Ms.")
    elif age < 16:
        print("Miss")
elif gender == "m":
    if age >= 16:
        print("Mr.")
    elif age < 16:
        print("Master")