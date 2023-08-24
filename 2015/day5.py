#!/usr/bin/python3


# nice == three or more vowels and at least one letter that appears twice in a row
# also must not contain 'ab', 'cd', 'pq', or 'xy'

def part1():
    with open('day5_data.txt', 'r') as file:
        data = file.read()

    lines = data.split('\n')


    vowels = ['a', 'e', 'i', 'o', 'u']

    for line in lines:
        if line.count('a') >= 3 and line.count('ab') == 0 and line.count('cd') == 0 and line.count('pq') == 0 and line.count('xy') == 0:
            print(line)

part1()
