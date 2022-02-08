count_floors = int(input())
count_rooms = int(input())

for floor in range(count_floors, 0, -1):
    # za vseki etaj iskame da minem prez vsqka edna staq
    for room in range(0, count_rooms):
        if floor == count_floors:
            print(f"L{floor}{room}", end=" ")
        elif floor % 2 == 1:
            print(f"A{floor}{room}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=" ")
    print()
