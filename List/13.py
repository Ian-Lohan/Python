#write a program to calculate the ideal weight of a person based on their gender with the following formulas
#if male = (72.7 * h) - 58
#if female = (62.1 * h) - 44.7
height = float(input('Enter your height: '))
gender = input('Are you male (m) or female (f): ')
if gender == 'm':
  iweight = ((72.7 * height) - 58)
  print ('Your ideal weight is %f' % (iweight))
else:
  iweight = ((62.1 * height) - 44.7)
  print ('Your ideal weight is %f' % (iweight))