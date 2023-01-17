name = input()
grade = 1
annual_grade = 0
fail = 0

while True:
    current_input = float(input())

    if current_input < 4.00:
        fail += 1
        if fail >= 2:
            break
        continue
    annual_grade += current_input
    grade += 1
    if grade > 12:
        break

if fail >= 2:
    print(f"{name} has been excluded at {grade} grade")
else:
    print(f"{name} graduated. Average grade: {annual_grade / 12:.2f}")
    