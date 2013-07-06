import math
def divisors(n):
	divs=set()
	divs.add(1)
	for i in range(2,int(math.sqrt(n))+1 ):
		if n % i == 0:
			divs.add(i)
			divs.add(int(n/i))
	return (divs)


#print(divisors(15))


a = set()
for i in range(10000):
	p = sum(divisors(i))
	if (sum(divisors(p)) == i and i != p):
		a.add(i)
		a.add(p)
print(a)
print(sum(a))