#!/usr/bin/python3

with open('day1_data.txt', 'r') as file:
    data = file.read()

# Part 1

def part1():

    floor = 0

    for i in range(len(data)):
        if data[i] == '(':
            floor += 1
        elif data[i] == ')':
            floor -= 1
        else:
            pass

    print('Part1 solution', floor)

part1()


# Part 2

def part2():

    floor = 0
    first_basement = 0

    for i in range(len(data)):
        if floor == -1:
            first_basement = i
            print('Part2 solution', first_basement)
            break
        else:
            if data[i] == '(':
                floor += 1
            elif data[i] == ')':
                floor -= 1
            else:
                pass
part2()
