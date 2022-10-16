from random import randint
def level():
  level= input("Choose your level 'easy' or 'hard': ")
  if level== 'hard':
    return 5
  else:
    return 10
    
compnum= randint(1, 100)

def dis(num):
  global compnum
  if compnum> num:
    print("Too Low")
  elif compnum< num:
    print("Too High")
  else:
    print("You Won!")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty= level()
if difficulty== 5:
  num=5
else:
  num=10
trial=0
guess=0
while trial in range(0,num) and compnum!=guess :
   guess= int(input("Enter Your guess: "))
   trial+=1
   guess+=guess
   print(f"You have {num-trial} attempts left")
   dis(guess)
if compnum==guess:
  print("You won")
else:
  print("You Failed")
