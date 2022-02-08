destination = input()

while destination != "End":
    need_money = int(input())
    money = 0
    while money < need_money:
        saved_money = int(input())
        money += saved_money
    else:
        print(f"Going to {destination}!")

    destination = input()