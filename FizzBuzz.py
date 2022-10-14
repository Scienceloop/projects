num= int(input("Enter your number: "))
n= range(1, num+1)
for N in n:
  if N%15 == 0:
    print("FizzBuzz")
  elif N%3==0:
    print("Fizz")
  elif N%5==0:
    print("Buzz")
  else:
    print(N)
