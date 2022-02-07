numbers = [int(num) for num in input().split()]
numbers_to_remove = int(input())

for number in range(numbers_to_remove):
    numbers.remove(min(numbers))

print(numbers)
