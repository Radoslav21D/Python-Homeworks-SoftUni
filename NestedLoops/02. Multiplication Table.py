# purvi mnojitel -> 1 do 10
# vseki purvi mnojitel * vtoriq (1, 10)
i = 0  # za debugera
for first in range(1, 11):
    for second in range(1, 11):
        result = first * second
        print(f"{first} * {second} = {result}")
        