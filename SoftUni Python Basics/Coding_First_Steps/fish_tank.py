length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = length * width * height / 1000
volume -= volume * percent

print(volume)
