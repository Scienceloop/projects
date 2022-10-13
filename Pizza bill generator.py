print("Welcome to Python Pizza Deliveries! \n Small Pizza: $15 \n Medium Pizza: $20 \n Large Pizza: $25 \n")
size = input("What size pizza do you want? S, M, or L ")
print('Pepperoni for Small Pizza: +$2 \n Pepperoni for Medium or Large Pizza: +$3')
add_pepperoni = input("Do you want pepperoni? Y or N ")
print("Extra cheese for any size pizza: + $1")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill= 0
if size== "S" :
  bill +=15
elif size== "M":
  bill+= 20
else:
  bill += 25
if add_pepperoni == "Y":
  if size== "S" :
    bill += 2
  else:
    bill+= 3
else:
  pass
if extra_cheese == "Y":
  bill+= 1
else:
  pass
print("Your final bill is: $"+ str(bill))
