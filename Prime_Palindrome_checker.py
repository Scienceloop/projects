num = int(input("Enter a number: "))
temp = num

def is_palindrome():
    global num
    global temp
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if (temp == rev):
        print("The number is palindrome!")
    else:
        print("This is Not a palindrome!")


def prime_checker():
    global temp
    is_prime = True
    for N in range(2, temp):
        if (temp % N) == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


is_palindrome()
prime_checker()

