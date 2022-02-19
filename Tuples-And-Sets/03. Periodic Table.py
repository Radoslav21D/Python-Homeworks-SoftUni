n = int(input())

elements = set()

for _ in range(n):
    [elements.add(x) for x in input().split()]

[print(x) for x in elements]
