#write a program that asks for 3 numbers then prints them in descending order
numbers = []
number1 = int(input('Insert the first integer: '))
numbers.append(number1)
number2 = int(input('Insert the second interger: '))
numbers.append(number2)
number3 = int(input('Insert the third integer: '))
numbers.append(number3)
numbers.sort(reverse=True)
print(numbers)