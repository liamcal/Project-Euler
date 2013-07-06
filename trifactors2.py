import functools
import math
def numFactors(n):

	return len(set(functools.reduce(list.__add__, ([i, n/i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0))))

def generateT(x):
	nums = [1]
	i = 2
	while i <= x:
		nums.append(nums[-1]+i)
		i+=1
	return nums

tri=generateT(10000000)

#print(tri)

for n in tri:
	if n % 10 == 0:
		count = numFactors(n)
		print(n, " has: ",count)
		if count > 500:
			print ("found", n)
			break