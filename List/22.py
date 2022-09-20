#write a program that asks for a letter, then prints if it`s a vowel or consonant
while True:
    letter = input('Enter a letter: ')
    if not letter.isalpha():
        print('Enter only letters')
        continue
    else:
        break
vowels = ['a','e','i','o','u']
if letter in vowels:
    print('The letter %s is a vowel.' % (letter))
else:
    print('The letter %s is a consonant.' % (letter))