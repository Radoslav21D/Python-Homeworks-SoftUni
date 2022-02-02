# крайна цена
# намаление спрямо стаята и нощувките
# доп. намаление спрямо оценката

days = int(input())
room_type = input()
grade = input()

final_price = 0
nights = days - 1

if room_type == "room for one person":
    final_price = nights * 18
elif room_type == "apartment":
    final_price = nights * 25
elif room_type == "president apartment":
    final_price = nights * 35

# крайна цена без намаление -> final_price
# намаление


if room_type == "apartment":
    if days < 10:
        final_price = final_price - 0.30 * final_price  # 0.7 * final_price
    elif 10 <= days <= 15:
        final_price = final_price - 0.35 * final_price  # 0.65 * final_price
    elif days > 15:
        final_price = final_price - 0.50 * final_price
elif room_type == "president apartment":
    if days < 10:
        final_price = final_price - 0.10 * final_price
    elif 10 <= days <= 15:
        final_price = final_price - 0.15 * final_price
    elif days > 15:
        final_price = final_price - 0.20 * final_price

if grade == "positive":
    final_price = final_price + 0.25 * final_price
elif grade == "negative":
    final_price = final_price - 0.10 * final_price
print(f"{final_price:2f}")
