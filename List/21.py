#write a program that asks for the name of 6 cities then prints the longest city name
#the program asks if you want to extend the name of the city
cities = []
for i in range (0,6):
    inputs = input('Please insert the name of the %d city: ' % (i + 1))
    if inputs in cities:
        inputs = input('That name is already in the list. Please insert the name of the city: ')
    cities.append(inputs)
    answer = input('Would you like to extend the city name?(y/n) ')
    if answer in ('Y', 'y'):
        extra = input('Input the name extension: ')
        cities[i] = cities[i] + extra
        print(cities[i])
print('The city names inputted are: ', *cities)
longest = max(cities,key=len)
print(longest,'is the longest city name!')