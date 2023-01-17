import math

world_record = float(input())
distance = float(input())
time_for_one_meter = float(input())

ivan_time = distance * time_for_one_meter
new_distance = math.floor(distance / 15)
slow_down = new_distance * 12.5
new_time = ivan_time + slow_down
insufficient_time = abs(world_record - new_time)
if world_record > new_time:
    print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {insufficient_time:.2f} seconds slower.")
