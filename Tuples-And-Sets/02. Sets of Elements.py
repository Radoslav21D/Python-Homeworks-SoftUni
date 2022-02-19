n, m = [int(x) for x in input().split()]

first = set()
second = set()
# first
for _ in range(n):
    first.add(input())
# second
for _ in range(m):
    second.add(input())
# intersection
result = first.intersection(second)
for el in result:
    print(el)
