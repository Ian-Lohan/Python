#write a program to ask for a number in a list and check if the number is in it, then print the number and it's index in the list
list = [1,2,3,4,5,6,7,8,9,0]
input = int(input('Input a number between 0 and 10: '))
while input not in list:
  input = int(input('Input a number between 0 and 10: '))
if input in list:
  index = list.index(input)
  print ('The number %d exists and it`s position in the list is %d' % (input, index))