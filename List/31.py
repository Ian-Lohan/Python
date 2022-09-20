#write a program to ask the user a few questions, then print if the user is innocent, suspect, accessory or assassin
answers = []
call = input('Have you called the victim?(y/n): ')
while call not in ('y', 'n'):
    print('Answer the question!')
    call = input('Have you called the victim?(y/n): ')
answers.append(call)
scene = input('Have you been to the crime scene?(y/n): ')
while scene not in ('y', 'n'):
    print('Answer the question!')
    scene = input('Have you been to the crime scene?(y/n): ')
answers.append(scene)
live = input('Do you live near the victim?(y/n): ')
while live not in ('y', 'n'):
    print('Answer the question!')
    live = input('Do you live near the victim?(y/n): ')
answers.append(live)
owe = input('Did you owe to the victim?(y/n): ')
while owe not in ('y', 'n'):
    print('Answer the question!')
    owe = input('Did you owe to the victim?(y/n): ')
answers.append(owe)
work = input('Did you work with the victim?(y/n): ')
while work not in ('y', 'n'):
    print('Answer the question!')
    work = input('Did you work with the victim?(y/n): ')
answers.append(work)
result = answers.count('y')
if result == 2:
    print('\nYou are a suspect.')
elif result == 3 or result == 4:
    print('\nYou are an accessory!')
elif result == 5:
    print('\nYou are the assassin!!!')