type_of_the_movie = input()
rows = int(input())
columns = int(input())
ticket_price = 0
total_sum = 0
if type_of_the_movie == "Premiere":
     ticket_price = 12
elif type_of_the_movie == "Normal":
    ticket_price = 7.50
elif type_of_the_movie == "Discount":
    ticket_price = 5
number_of_tickets = rows * columns
total_sum = number_of_tickets * ticket_price
print(f"{total_sum:.2f} leva")
