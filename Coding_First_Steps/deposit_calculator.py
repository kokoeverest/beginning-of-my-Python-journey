deposit = float(input())
time = int(input())
annual_loan_interest = float(input()) / 100

total_money = deposit + time * ((deposit * annual_loan_interest) / 12)

print(total_money)
