#!/usr/bin/python3

# measurements l * w * h
# surface area = 2*l*w + 2*w*h + 2*h*l
# extra = area of the smallest side, 1 side.

with open('day2_data.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')



for line in lines:
    x = line.split('x')
    print([x])
