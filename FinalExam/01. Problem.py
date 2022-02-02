text = input()
current_text = ""
command = input()
while not command == "Done":
    data = command.split()
    action = data[0]
    if action == "Change":
        char = data[1]
        replacement = data[2]
        if char in text:
            current_text = text.replace(char, replacement)
            print(current_text)
            text = current_text
        else:
            print(text)

    if action == "Includes":
        string = data[1]
        if string in text:
            print(True)
        else:
            print(False)

    if action == "End":
        string = data[1]
        print(text.endswith(string))

    if action == "Uppercase":
        current_text = text.upper()
        print(current_text)
        text = current_text

    if action == "FindIndex":
        char = data[1]
        for index in range(len(text)):
            if char == text[index]:
                print(index)
                break

    if action == "Cut":
        start_index = int(data[1])
        end_index = int(data[2]) + start_index
        print(text[start_index:end_index])


    command = input()