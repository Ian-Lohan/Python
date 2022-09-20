#write a program that asks for 3 numbers, then prints the highest and lowest ones
n = []
n1 = float(input('Insert first number: '))
n.append(n1)
n2 = float(input('Insert second number: '))
n.append(n2)
n3 = float(input('Insert third number: '))
n.append(n3)
n.sort()
print('The lowest number is %.2f\nThe highest number is %.2f' % (n[0], n[-1]))