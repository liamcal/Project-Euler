import math
number = 600851475143
def is_prime(n):
    if n == 2 or n == 3: 
        return True
    elif n < 2 or n % 2 == 0: 
        return False
    elif n < 9:
        return True
    elif n % 3 == 0: 
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0: 
            return False
        else:
            f += 6
    return True

for i in range(1,number):
    if (number % i == 0):
        print("testing ",i)
        if (is_prime(i)):
            highest = i
            print (i, " is prime")

