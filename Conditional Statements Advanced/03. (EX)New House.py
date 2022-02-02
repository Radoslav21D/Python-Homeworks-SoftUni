type_of_flowers = input()
quantity_of_flowers = int(input())
budget = int(input())
price_per_flower = 0
total_sum = 0

if type_of_flowers == "Roses":
    price_per_flower = 5
    if quantity_of_flowers > 80:
        price_per_flower *= 0.9
elif type_of_flowers == "Dahlias":
    price_per_flower = 3.80
    if quantity_of_flowers > 90:
        price_per_flower *= 0.85
elif type_of_flowers == "Tulips":
    price_per_flower = 2.80
    if quantity_of_flowers > 80:
        price_per_flower *= 0.85
elif type_of_flowers == "Narcissus":
    price_per_flower = 3
    if quantity_of_flowers < 120:
        price_per_flower *= 1.15
elif type_of_flowers == "Gladiolus":
    price_per_flower = 2.50
    if quantity_of_flowers < 80:
        price_per_flower *= 1.20

total_sum = quantity_of_flowers * price_per_flower
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"Hey, you have a great garden with {quantity_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")


