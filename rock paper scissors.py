rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
my_list= [rock,paper,scissors]
print(my_list[user])
import random
c= random.randint(0,2)
print(f"Computer \n {my_list[c]}" )
if user<c:
  print("You Lost")
elif user==c:
  print("Draw")
else:
  print("You Win")
