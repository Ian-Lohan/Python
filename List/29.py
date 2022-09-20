#write a program that asks for a salary and adjusts it based on the value
#then prints the new salary and the changes
salary = float(input('Insert the current salary: '))
if salary < 280:
    adjustment = 1.2
    new_salary = salary * adjustment
elif salary >= 280 and salary < 700:
    adjustment = 1.15
    new_salary = salary * adjustment
elif salary >= 700 and salary < 1500:
    adjustment = 1.1
    new_salary = salary * adjustment
elif salary >= 1500:
    adjustment = 1.05
    new_salary = salary * adjustment
print('Old salary: %.2f, Adjustment Percentage: %.2f, Adjustment value: %.2f, New salary: %.2f' % (salary, adjustment, new_salary - salary, new_salary))