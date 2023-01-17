from math import ceil
movie_name = input()
movie_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8 #or 1/8 * break_duration
relax_time = break_duration / 4

total_time_needed = lunch_time + relax_time + movie_duration

if break_duration >= total_time_needed:
    print(f"You have enough time to watch {movie_name} and left with {ceil(break_duration - total_time_needed)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(total_time_needed - break_duration)} more minutes.")

x = 0
# Изход
# На конзолата да се изпише един ред:
#     • Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
#     • Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
# Времето да се закръгли до най-близкото цяло число нагоре.