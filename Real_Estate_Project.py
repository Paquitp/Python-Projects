price_house = 1_000_000.0

credit_score = int(input("Your Credit Score: "))
 
if credit_score >= 700:
  good_credit = credit_score
  print("Downpayment Rate: 10%")
  print("Downpayment amount: $" + str(price_house*.10))
  total_cost= (price_house*.10 + price_house)
else:
  print("Downpayment Rate: 20%")
  print("Downpayment amount: $" + str(price_house*.20))
  total_cost= (price_house*.20 + price_house)

 

print("Your total balance + Downpayment: $" + str(total_cost))
print("Done")
