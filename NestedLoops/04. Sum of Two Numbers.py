# chislo 1 -> [start, end]
# chislo 2 -> [start, end]
start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
isFound = False

for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        counter += 1
        # vsichki kombinacii
        if first_number + second_number == magic_number:
            print(f"Combination N:{counter} ({first_number} + {second_number} = {magic_number})")
            isFound = True
            break
    if isFound:
        break

else:
    print(f"{counter} combinations - neither equals {magic_number}")
