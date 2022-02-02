count = int(input())

for _ in range(count):
    valid = False
    tokens = input().split(':')

    if tokens[0][0] in ['$', '%'] and tokens[0][0] == tokens[0][-1]:
        tkn = tokens[0][1:-1]
        if len(tkn) > 2 and tkn[0].isupper():
            vl = True
            for letter in tkn[1:]:
                if not letter.islower():
                    vl = False

            if vl:
                valid = True


    if valid:
        tkn = tokens[0][1:-1]
        tkns2 = tokens[1].split('|')
        if tkns2[-1] != '':
            print('Valid message not found!')
            continue
        tkns2.pop()
        if len(tkns2) > 3:
            print('Valid message not found!')
            continue
        tkn2 = ''
        for ls in tkns2:
            letter = ls.replace(' ', '').replace('[', '').replace(']', '')
            tkn2 += chr(int(letter))
        print(f'{tkn}: {tkn2}')
    else:
        print('Valid message not found!')
