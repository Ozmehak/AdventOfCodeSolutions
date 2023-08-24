#!/usr/bin/python3

import hashlib

puzzle_input = 'bgvyzdsi' 
encoded_input = hashlib.md5(puzzle_input.encode())

hexa = encoded_input.hexdigest()
print(hexa)
