#write a program that asks for your school turn, then prints the right greeting
accept = ['M','m','V','v','N','n']
turn = input('Please insert which turn you study in (M = Matutino, V = Vespertino, N = Noturno): ')
while True:
    if turn not in accept:
        turn = input('Invalid Input. Please insert which turn you study in (M = Matutino, V = Vespertino, N = Noturno): ')
        continue
    else:
        break
if turn == ('M' or 'm'):
    print('Good Morning!')
elif turn == ('V' or 'v'):
    print('Good Afternoon!')
elif turn == ('N' or 'n'):
    print('Good Evening!')