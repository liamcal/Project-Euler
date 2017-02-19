import math
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

def quad(n,a,b):
    return (n*n + a*n + b)
maxn=0
maxa=0
maxb=0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0
        while True:
            if(is_prime(quad(n,a,b))):
                n+=1
            else:
                if n > maxn:
                    maxn=n
                    maxa=a
                    maxb=b
                    print("new max: ",n, "with a", a, "and b", b)
                break
print("Largest n:",maxn, "with a",maxa, "and b",maxb)
