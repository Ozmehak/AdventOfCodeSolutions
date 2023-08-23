#!/usr/bin/python3



with open('day3_data.txt', 'r') as file:
          data = file.read()
          
          

santa_x = 0
santa_y = 0
robot_x = 0
robot_y = 0

santa_coordinates = []
robot_coordinates = []

#first house
santa_coordinates.append([santa_x, santa_y])
robot_coordinates.append([robot_x, robot_y])

for i in range(0, len(data), 2):
    match data[i]:
        case '>':
            santa_x += 1
            santa_coordinates.append([santa_x, santa_y])
        case '<':
            santa_x -= 1
            santa_coordinates.append([santa_x, santa_y])
        case 'v':
            santa_y -= 1
            santa_coordinates.append([santa_x, santa_y])
        case '^':
            santa_y += 1
            santa_coordinates.append([santa_x, santa_y])


for i in range(1, len(data), 2):
    match data[i]:
        case '>':
            robot_x += 1
            robot_coordinates.append([robot_x, robot_y])
        case '<':
            robot_x -= 1
            robot_coordinates.append([robot_x, robot_y])
        case 'v':
            robot_y -= 1
            robot_coordinates.append([robot_x, robot_y])
        case '^':
            robot_y += 1
            robot_coordinates.append([robot_x, robot_y])




santa_coordinates_no_duplicates = {} 
santa_and_robot_coordinates_no_duplicates = {}
print(data)
print(len(data))
print(len(santa_coordinates))
print(len(robot_coordinates))

for coordinate in santa_coordinates:
    santa_and_robot_coordinates_no_duplicates[santa_coordinates.index(coordinate)] = coordinate

for coordinate in robot_coordinates:
    santa_and_robot_coordinates_no_duplicates[robot_coordinates.index(coordinate)] = coordinate


print('houses with robot', len(santa_and_robot_coordinates_no_duplicates))
# print(santa_and_robot_coordinates_no_duplicates)


# for coordinate in santa_coordinates:
#     santa_coordinates_no_duplicates[santa_coordinates.index(coordinate)] = coordinate

# print(len(santa_coordinates_no_duplicates))
# print(len(santa_coordinates))
#
