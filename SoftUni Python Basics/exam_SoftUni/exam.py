students = int(input())

excellent_students = 0
very_good_students = 0
good_students = 0
fails = 0
total_grades = 0

for i in range(students):
    grade = float(input())
    if grade >= 5.00:
        excellent_students += 1
        total_grades += grade
    elif grade < 5.00 and grade >= 4.00:
        very_good_students += 1
        total_grades += grade
    elif grade < 4.00 and grade >= 3.00:
        good_students += 1
        total_grades += grade
    elif grade < 3.00 and grade >= 2.00:
        fails += 1
        total_grades += grade

print(f'Top students: {excellent_students / students * 100:.2f}%')
print(f'Between 4.00 and 4.99: {very_good_students / students * 100:.2f}%')
print(f'Between 3.00 and 3.99: {good_students / students * 100:.2f}%')
print(f'Fail: {fails / students * 100:.2f}%')
print(f'Average: {total_grades / students:.2f}')
# Напишете програма, която да пресмята статистика за оценки от изпит. В началото програмата получава броя
# на студентите явили се на изпита и за всеки студент неговата оценка. На края програмата трябва да отпечата
# процента студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също
# така и средния успех на изпита.
'''
# Вход:
# От конзолата се четат:
#  На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
#  За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
'''
# Изход:
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 - "Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 - "Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 - "Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 - "Fail: {по-малко от 3.00}%"
# Ред 5 - "Average: {среден успех}"
# Всички числа трябва да са форматирани до втория знак след десетичната запетая.