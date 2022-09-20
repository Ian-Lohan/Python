#write a program to register the name, gender, height, weight, cpf of 3 people.
#then locate the person with the cpf and print their imc
people = []
while True:
    person = []
    name = input('\nInput the person name: ')
    gender = input('Input your gender (m/f): ')
    while gender not in ('M', 'm', 'F', 'f'):
        print('You must be either M or F!')
        gender = input('Input your gender (m/f): ')
    height = float(input('Input your height in meters: '))
    weight = float(input('Input your weight in kg: '))
    cpf = input('Input your CPF: ')
    while len(cpf) != 11:
        print('The CPF inputted is not 11 digits long!')
        cpf = input('Input your CPF: ')
    imc = (weight / (height * height))
    person.append(name)
    person.append(gender)
    person.append(height)
    person.append(weight)
    person.append(cpf)
    person.append(imc)
    people.append(person)
    answer = input('\nWould you like to add another person?(y/n) ')
    if answer in ('Y', 'y'):
        continue
    elif answer in ('N', 'n'):
        break
    else:
        print('Invalid Input!')
        answer = input('\nWould you like to add another person?(y/n) ')
call = input('\nInput a cpf to find a person: ')
while len(call) != 11:
    print('The CPF inputted is not 11 digits long!')
    call = input('Input a cpf to find a person: ')
for elem in people:
    if call in elem:
        print('\n')
        print(elem)