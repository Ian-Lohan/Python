#write a program that calculates the payment
hour_value = float(input('Insert the value per hour: '))
hours_month = float(input('Insert the amount of work hours per month: '))
raw_salary = hour_value * hours_month
if raw_salary <= 900:
    ir_discount = 0
elif raw_salary <= 1500:
    ir_discount = 0.05
elif raw_salary <= 2500:
    ir_discount = 0.1
elif raw_salary > 2500:
    ir_discount = 0.2
if raw_salary > 900:
    ir_salary = (raw_salary * ir_discount)
elif raw_salary <= 900:
    ir_salary = 0
inss = 1.1
inss_salary = (raw_salary * inss) - raw_salary
fgts = 1.11
fgts_salary = (raw_salary * fgts) - raw_salary
total_discount = inss_salary + ir_salary
liquid_salary = raw_salary - total_discount
print ('Raw Salary(%.2f * %.2f): %.2f\nIR(%.2f): %.2f\nINSS(%.2f): %.2f\nFGTS(%.2f): %.2f\nDiscount Total: %.2f\nLiquid Salary: %.2f' % (hour_value, hours_month, raw_salary, ir_discount, ir_salary, inss, inss_salary, fgts, fgts_salary, total_discount, liquid_salary))