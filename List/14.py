#write a code to check the excess beyond the kg 50 and add a fine of 4 real for each kg
kg = int(input('How many kg of fish? '))
excess = kg - 50
if excess >= 1:
  fine = excess * 4
  print ('Your fine is %d real' % (fine))
else:
  print ('There`s no fine for you!')