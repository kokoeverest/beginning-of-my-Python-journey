from math import pi

figure = input()

if figure == 'square':
    length = float(input())
    area = length * length
elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == 'circle':
    radius = float(input())
    area = pi * (radius * radius)
elif figure == 'triangle':
    length_of_side = float(input())
    height_of_side = float(input())
    area = (1/2 * length_of_side) * height_of_side

print(figure)
print(f'{area:.3f}')
