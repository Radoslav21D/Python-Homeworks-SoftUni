hours = int(input())
day = input()

is_open = False
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if 10 <= hours<= 18:
        is_open = True
if is_open == True:
    print("open")
else:
    print("closed")
