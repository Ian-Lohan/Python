#write a program that asks for 4 scores then prints the average of them
import statistics
a = int(input('Enter the first score between 1 and 10: '))
b = int(input('Enter the second score between 1 and 10: '))
c = int(input('Enter the third score between 1 and 10: '))
d = int(input('Enter the fourth score between 1 and 10: '))
score = [a,b,c,d]
average = statistics.mean(score)
print ('The average is ', average)