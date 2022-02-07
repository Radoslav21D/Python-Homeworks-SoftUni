stack = input().split()
result = []

# докато имаме стек:
while stack:
    el = stack.pop()
    result.append(el)

# .join за да може изхода да е на един ред
print(' '.join(result))
