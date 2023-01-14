number = int(input())
counter = 0

for n in range(1, number + 1):
    for o in range(1, n + 1):
        counter += 1

        print(f'{counter}', end=" ") if n != o else print(f'{counter}')

        if counter == number:
            raise SystemExit

# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида от числа като в примерите: