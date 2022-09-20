#write a program that asks for 2 grades then prints the average
grade1 = float(input('Insert the first grade between 0 and 10: '))
while grade1 < 0 or grade1 > 10:
    print('Grade not accepted.')
    grade1 = float(input('Insert the first grade between 0 and 10: '))
    continue
grade2 = float(input('Insert the second grade between 0 and 10: '))
while grade2 < 0 or grade2 > 10:
    print('Grade not accepted.')
    grade2 = float(input('Insert the second grade between 0 and 10: '))
    continue
average = (grade1 + grade2) / 2
print('Your average grade is %.2f' % (average))
if average >= 7:
    print('Approved!')
elif average == 10:
    print('VERY Approved!')
else:
    print('Not Approved!')