number_one, number_two = int(input()), int(input())

for number in range(number_one, number_two + 1):
    even_sum, odd_sum = 0, 0

    for index, digit in enumerate(str(number)):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if odd_sum == even_sum:
        print(number, end=" ")

# Напишете програма, която чете от конзолата две шестцифрени цели числа. Винаги първото въведено число ще бъде по-малко /
# от второто. На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа, които се намират между двете, /
# прочетени от конзолата числа и отговарят на условието сумата от цифрите на четни и нечетни позиции да са равни. /
# Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.