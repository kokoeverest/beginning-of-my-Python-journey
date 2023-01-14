bad_result = int(input())
problems = 0
bad_grade = 0
total_grades = 0
current_task = ""

while bad_grade < bad_result:
    task = input()

    if task == "Enough":
        print(f"Average score: {total_grades / problems:.2f}")
        print(f"Number of problems: {problems}")
        print(f"Last problem: {current_task}")
        break

    grade = int(input())

    if grade <= 4:
        bad_grade += 1

    total_grades += grade
    problems += 1
    current_task = task
else:
    print(f"You need a break, {bad_grade} poor grades.")
    # Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си. /
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда /
# "Enough" или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е /
# по-малка или равна на 4.
# Вход
#     • На първи ред - брой незадоволителни оценки - цяло число;
#     • След това многократно се четат по два реда:
#         ◦ Име на задача – текст;
#     • Оценка - цяло число в интервала [2…6]
# Изход
#     • Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
#     • "Average score: {средна оценка}"
#     • "Number of problems: {броя на всички задачи}"
#         ◦ "Last problem: {името на последната задача}"
#     • Ако получи определеният брой незадоволителни оценки:
#     • "You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.