print(print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''))
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
crossroad= input("""You're at a crossroad. Where do you want to go? Type "left" or "right" """)
if crossroad.lower() == "left":
   print("You fell into a hole. Game Over.")
else:
  lake= input(""""You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.""")
  if lake.lower() == "swim":
    print("You get attacked by an angry trout. Game Over.") 
  else:
    door = input("""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one 
 blue. Which colour do you choose?""")
    if door.lower() == "blue":
      print('''                                                                    
                                                                       ,d     
                                                                       88     
 ,adPPYba,  ,adPPYba,  8b,dPPYba,   ,adPPYb,d8 8b,dPPYba, ,adPPYYba, MM88MMM  ,adPPYba,  
a8"     "" a8"     "8a 88P'   `"8a a8"    `Y88 88P'   "Y8 ""     `Y8   88     I8[    "" 
8b         8b       d8 88       88 8b       88 88         ,adPPPPP88   88     `"Y8ba,
"8a,   ,aa "8a,   ,a8" 88       88 "8a,   ,d88 88         88,    ,88   88,  aa    ]8I
 `"Ybbd8"'  `"YbbdP"'  88       88  `"YbbdP"Y8 88         `"8bbdP"Y8   "Y888 `"YbbdP"'
                                    aa,    ,88                                
                                     "Y8bbdP"                                   
           ''')
    else:
      print("Game Over")

#Write your code below this line 👇

