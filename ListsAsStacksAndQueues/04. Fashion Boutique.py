clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_racks = 1
current_rack_capacity = rack_capacity
while clothes:
    clothing = clothes[-1]
    if clothing > current_rack_capacity:
        used_racks += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= clothing
        clothes.pop()

print(used_racks)
