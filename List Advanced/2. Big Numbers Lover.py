# input
numbers_as_strings = input().split()
# sorting and reversing the numbers as strings
numbers_desc_as_strings = sorted(numbers_as_strings, reverse=True)
# output
print("".join(numbers_desc_as_strings))
