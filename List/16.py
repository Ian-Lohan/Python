#write a program that asks you how big is the area to be painted, then calculates the price of the paint to be bought to paint it
area = int(input('How big is the area to be painted in meters squared? '))
meters = area / 3
if area % 54 == 0:
  can = area / 54
else:
  can = int(area / 54) + 1
price = can * 80
print ('You need %d cans' %can)
print ('R$ %.2f' %price)