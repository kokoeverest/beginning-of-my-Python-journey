total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break
    free_seats = int(input())
    current_tickets = 0

    while current_tickets < free_seats:
        ticket_type = input()

        if ticket_type == "End":
            break

        total_tickets += 1
        current_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
    print(f'{movie_name} - {(current_tickets / free_seats) * 100:.2f}% full.')

print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.')


# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети:/
# студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента /
# от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
#     • На първия ред до получаване на командата "Finish" - име на филма – текст
#     • На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
#     • За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
#         ◦ Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
#     • След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full.
# • При получаване на командата "Finish" да се отпечатат четири реда:
# ◦ "Total tickets: {общият брой закупени билети за всички филми}"
# ◦ "{процент на студентските билети}% student tickets."
# ◦ "{процент на стандартните билети}% standard tickets."
# ◦ "{процент на детските билети}% kids tickets."