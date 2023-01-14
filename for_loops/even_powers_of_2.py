from math import pow

n = int(input())

for i in range(0, n + 1, 2):
    print(int(pow(2, i)))

# Да се напише програма, която чете число n, въведено от потрeбителя, и печата четните степени на 2 ≤ 2n: 20, 22, 24, 26, …, 2n.