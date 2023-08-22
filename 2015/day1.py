#!/usr/bin/python3

with open('day1_data.txt', 'r') as file:
    data = file.read()
    print(len(data))

    floor = 0
    first_basement = 0

    for i in range(len(data)):
        if floor == -1:
            first_basement = i
            print(first_basement)
            break
        else:
            if data[i] == '(':
                floor += 1
            elif data[i] == ')':
                floor -= 1
            else:
                pass

    print(floor)

