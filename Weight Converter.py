weight = float(input("Your Weight: "))
unit = str(input("Unit: (K)g or (L)bs"))
if unit.upper() == "k":  
 converted = weight / 0.45
 print("Your weight in Lbs: " + str(converted))
else: 
  converted = weight * 0.45
  print("Your weight in Kg: " + str(converted))
