number_of_cats = int(input())
grams_of_food = float(input())
food_price = 12.45
group1 = 0
group2 = 0
group3 = 0

for i in range(number_of_cats):

    if 100 <= grams_of_food < 200:
        group1 += 1
    if 200 <= grams_of_food < 300:
        group2 += 1
    if 300 <= grams_of_food < 400:
        group3 += 1
sum_of_grams_food = grams_of_food - number_of_cats
print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(sum_of_grams_food)
