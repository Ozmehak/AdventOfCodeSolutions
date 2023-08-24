#!/usr/bin/python3


# nice == three or more vowels and at least one letter that appears twice in a row
# also must not contain 'ab', 'cd', 'pq', or 'xy'

def part1():
    with open('day5_data.txt', 'r') as file:
        data = file.read()

    lines = data.split('\n')


    vowels = ['a', 'e', 'i', 'o', 'u']

    for line in lines:
        if vowels in line:
            print(line)
