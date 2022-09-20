#write a program that asks for 3 words, then prints the longest word and the number of characters in it
word1 = input('Enter the first word: ')
length1 = len(word1)
word2 = input('Enter the second word: ')
length2 = len(word2)
word3 = input('Enter the third word: ')
length3 = len(word3)
if length1 > length2 and length3:
    print('%s is the longest word, with %d characters' % (word1, length1))
elif length2 > length1 and length3:
    print('%s is the longest word, with %d characters' % (word2, length2))
elif length3 > length1 and length2:
    print('%s is the longest word, with %d characters' % (word3, length3))
else:
    print('Two or more words are the same length.')