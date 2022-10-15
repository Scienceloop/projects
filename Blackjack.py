def startgame():
    import random
    
    def card(cards):
      mycard_i= random.randrange(len(cards))
      return cards[mycard_i] 
      
    if start== "y":
      pass
    else:
      print("ok")
    
    from art import logo
    print(logo)
    cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    mycard1= card(cards)
    mycard2= card(cards)
    compcard1= card(cards)
    compcard2= card(cards)
    print(f"Your cards: {[mycard1, mycard2]}")
    print(f"Computer's card {compcard1}")
    play= input("Type 'y' to get another card, type 'n' to pass: ")
    if play== "y":
      mycard3= card(cards)
      finalscore= mycard1+ mycard2+ mycard3
      print(f"Your final cards: {[mycard1, mycard2, mycard3]}, Final score {finalscore}")
    else:
      finalscore= mycard1+ mycard2
      print(f"Your final cards: {[mycard1, mycard2]}, Final score {finalscore}")
    finalscorec= compcard1+ compcard2
    
    print(f"Computer's final cards: {[compcard1, compcard2]}, Final score {finalscorec} ")
    if finalscore > 21 or finalscore < finalscorec:
      print("You went over. You Loose")
    elif finalscore == finalscorec:
      print("Draw match")
    else:  
      print("You win")
    
    

start= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while start == "y":
  startgame()
