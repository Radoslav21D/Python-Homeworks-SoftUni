import re

text_line = input()
pattern = r"\d+"
all_numbers = []

while not text_line == "":
    numbers = re.findall(pattern, text_line)
    all_numbers.extend(numbers)
    text_line = input()

print(*all_numbers)
