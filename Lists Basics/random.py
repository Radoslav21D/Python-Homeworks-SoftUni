n = int(input())

evens = []
odds = []
positives = []
negatives = []

for _ in range(n):
    current_number = int(input())

    if current_number % 2 == 0:
        evens.append(current_number)

    if current_number < 0:
        negatives.append(current_number)

    if current_number >= 0:
        positives.append(current_number)

command = input()

if command == "even":
    print(evens)
elif command == "odd":
    print(odds)
elif command == "positive":
    print(positives)
else:
    print(negatives)
