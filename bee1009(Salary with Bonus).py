name = input()
salary = float(input())
sale = float(input())

seller_bonus = (15/100)*sale
t_salary = salary + seller_bonus

print("TOTAL = R$ %.2f" %t_salary)