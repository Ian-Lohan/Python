#write a program that asks how many hours a day and how many days in a month you work, then prints the monthly earnings
earn = int(input('How much do you earn per work hour? '))
hours = int(input('How many hours a day do you work? '))
monthly = earn * hours * 30
print ('You earn %d in a month' % (monthly))