command = input()

id_data = {}

while not command == 'End':
    company, id = command.split(' -> ')
    if company not in id_data:
        id_data[company] = []
        id_data[company].append(id)
    else:
        if id not in id_data[company]:
            id_data[company].append(id)

    command = input()

id_data = dict(sorted(id_data.items()))

for keys in id_data:
    print(keys)
    for id in id_data[keys]:
        print(f'-- {id}')
