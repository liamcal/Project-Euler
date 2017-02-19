from decimal import Decimal
from fractions import Fraction
def gen_iter(n,x=0):
	total = 0
	for i in range(n):
		 if i == 0:
		 	total = 2
		 if i == n-1:
		 	total = 1 + Fraction(1/total)
		 else:
		 	total = 2 + Fraction(1/total)
	return (Fraction(total))
count = 0
for i in range(1,1001):
	f = str(gen_iter(i))
	numerator = f.split('/')[0]
	denominator = f.split('/')[1]
	if len(numerator) > len(denominator):
		print('found',i)
		count += 1
print(count)
		
	
