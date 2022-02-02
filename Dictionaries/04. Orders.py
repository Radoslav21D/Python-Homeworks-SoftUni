data = input()

product_prices = {}
product_quantities = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in product_prices:
        product_prices[name] = price
        product_quantities[name] = quantity
    else:
        product_prices[name] = price
        product_quantities[name] += quantity

    data = input()

for product, price in product_prices.items():
    result = price * product_quantities[product]
    print(f"{product} -> {result:.2f}")
