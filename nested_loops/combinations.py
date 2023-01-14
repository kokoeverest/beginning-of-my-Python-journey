n = int(input())
operations = 0
for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            result = x1 + x2 + x3
            if result == n:
                operations += 1

print(operations)


# Напишете програма, която изчислява колко решения в естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n
# Числото n е цяло число и се въвежда от конзолата.