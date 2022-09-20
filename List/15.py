#write a program that asks how many hours a day and how many days in a month you work, then prints:
#the raw wage
#how much you paid the IR (-11%)
#how much you paid the INSS (-8%)
#how much you paid the Sindicate (-5%)
#the liquid wage
earn = int(input('How much do you earn per work hour? '))
hours = int(input('How many hours a day do you work? '))
wage = earn * hours * 30
ir = (wage * (11 / 100))
inss = (wage * (8 / 100))
sindicate = (wage * (5 / 100))
liquid = (wage - (ir + inss + sindicate))
print ('You earn %d raw wage in a month, and paid %f to the ir, %f to the inss, %f to the sindicate and the liquid wage is %f' % (wage, ir, inss, sindicate, liquid))