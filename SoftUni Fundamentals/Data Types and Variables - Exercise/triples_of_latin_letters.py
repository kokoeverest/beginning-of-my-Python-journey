"""
 my solution

number = int(input())

count1 = 0
count2 = 0
count3 = 0
while True:
    for a in range(97, 123):
        count1 += 1
        for b in range(97, 123):
            count2 += 1
            for c in range(97, 123):
                print(f'{chr(a)}{chr(b)}{chr(c)}')
                count3 += 1
                if count3 == number:
                    count3 = 0
                    break
            if count2 == number:
                count2 = 0
                break
        if count1 == number:
            exit()

            """

# solution by SoftUni

num = int(input())

for i in range(0, num):
    for j in range(0, num):
        for k in range(0, num):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')


# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically: