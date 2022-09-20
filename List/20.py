#write a program to compare inputted answers with a correct answers list, then print the percentage of correct
#answers and print if the user is approved or not if their percentage is equal or higher than 70%
print ('Please answer the 20 questions with a, b, c, d or e\n')
correct = ('a','c','d','d','e','b','c','c','a','b','d','c','b','e','c','b','a','e','b','c')
answers = []
n = 20
for i in range (0,20):
    ele = input('Insert answer of question %d: ' % (i + 1))
    answers.append(ele)
correct = sum(a == b for a, b in zip(correct, answers))
overlap = correct / len(answers) * 100
if overlap >= 60.0:
  print('You got a score of %d, you are APPROVED!' % (overlap))
else:
  print('You got a score of %d, you are NOT APPROVED!' % (overlap))