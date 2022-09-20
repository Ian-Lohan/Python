#write a program that asks you how big is the area to be painted, then calculates the price of the paint to be bought to paint it in cans or gallons
#then print: the price in cans to paint the area, the price in gallons and the price with both mixed
area = int(input('How big is the area to be painted in meters squared? '))
liters = area / 6
can = liters / 18
gallon = liters / 3.6
if can % 18 != 0:
  can += 1
pricec = can * 80
if gallon % 3.6 != 0:
  gallon += 1
priceg = gallon * 25
mix_can = int(liters / 18.0)
mix_gallon = int((liters - (mix_can * 18)) / 3.6)
if liters - (mix_can * 18) % 3.6 != 0:
  mix_gallon += 1
print ('If buying only cans. You need %d cans for R$ %.2f' % (can, pricec))
print ('If buying only gallons. You need %d gallons for R$ %.2f' % (gallon, priceg))
print ('If buying both cans and gallons. You need %d cans and %d gallons for R$ %.2f' % (mix_can, mix_gallon, ((mix_can * 80) + (mix_gallon * 25))))
