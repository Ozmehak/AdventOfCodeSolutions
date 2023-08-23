#!/usr/bin/python3

# measurements l * w * h
# surface area = 2*l*w + 2*w*h + 2*h*l
# extra = area of the smallest side, 1 side.

with open('day2_data.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')

paper_needed = 0
ribbon_needed = 0

for line in lines:
    measurements = line.split('x')
    if len(measurements) == 3:
        l, w, h = map(int, measurements)
        surface_area = 2*(l*w) + 2*(w*h) + 2*(h*l)
        extra = min((l*w), (w*h), (h*l))
        paper_needed += surface_area + extra

        # ribbon, sum of 2 smallest measurements and add l*w*h 
        smallest_sum = (2*l) + (2*w) + (2*h) - (max(l, w, h) * 2) 
        bow = (l*w*h)
        ribbon_needed += smallest_sum + bow
    else:
        pass
    
print('paper:', paper_needed)
print('ribbon:', ribbon_needed)
