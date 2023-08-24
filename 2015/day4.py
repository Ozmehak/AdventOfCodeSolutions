#!/usr/bin/python3

import hashlib

def part1():

    found = False
    correct_hash = '' 
    increment = 0

    while found == False:
        secret_key = 'bgvyzdsv'
        puzzle_input = secret_key + str(increment)
        encoded_input = hashlib.md5(puzzle_input.encode())
        hexa = encoded_input.hexdigest()
        print(hexa[0:6])
        if hexa[0:6] == '000000':
            found = True
            correct_hash += hexa
            print(correct_hash)
            print(puzzle_input)

        increment = increment + 1 
part1()
