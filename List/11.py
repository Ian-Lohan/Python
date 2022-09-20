#write a program that asks for 2 integers and a float, then prints
#the product of the double of the first summed with half of the second
#the sum of the triple of the first with the third
#the third number to the cube
first = int(input('Enter the first integer: '))
second = int(input('Enter the second integer: '))
third = float(input('Enter the float: '))
print ('\nThe product of the double of the first summed with half of the second is %d\n' % ((first * 2) * (second / 2)))
print ('The sum of the triple of the first with the third is %f\n' % ((first * 3) + third))
print ('The third number cubed is %f' % (third * third * third))