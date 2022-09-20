#create a program that registers 13 students, each with a name, password, two grades and their average, then print them all
students = []
for i in range(13):
    student = []
    print(f"\nYou are working on student {i+1}")
    name = input('Input the name of the student: ')
    password = input('Input the 8 digit password: ')
    while len(password) != 8:
        print('Password is not 8 digits long!')
        password = input('Input the 8 digit password: ')
    grade1 = float(input('Input the first grade between 0 and 10: '))
    while grade1 < 0 or grade1 > 10:
        print('Invalid grade!')
        grade1 = float(input('Input the first grade between 0 and 10: '))
    grade2 = float(input('Input the second grade between 0 and 10: '))
    while grade2 < 0 or grade2 > 10:
        print('Invalid grade!')
        grade2 = float(input('Insert the second grade between 0 and 10: '))
    average = (grade1 + grade2) / 2
    student.append(name)
    student.append(password)
    student.append(average)  
    print(student)
    students.append(student)
for i in range (13):
    print(students[i])