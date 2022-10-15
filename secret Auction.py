from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def winner(bid_list):
  hbid= 0
  for bidder, value in bid_list.items():
    if value> hbid:
      hbid= value
  winner= bidder
  print(f"Higest bidder is {winner} with value of ₹{hbid}")   

  
print(logo)
print("Welcome to the Auction")
bidder = "yes"
while bidder== "yes" :
  name= input("Enter your Name: ")
  bid= int(input("Enter your bidding ammount: "))
  bidder= input("Are there any Other Bidders? (yes/no)")
  bid_lists ={name:bid}
  if bidder== "yes":
    clear()
winner(bid_lists)
