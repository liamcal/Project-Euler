def generateT(x):
	nums = [1]
	i = 2
	while i <= x:
		nums.append(nums[-1]+i)
		i+=1
	return nums

tri=generateT(100000)

def numFactors(num):
	factors = []
	for i in range(1, int(num/2)):
		if num % i == 0:
			factors.append(i)
	return len(factors)

#print(tri)

for n in tri:
	count = numFactors(n)
	print(n, " has: ",count)
	if count > 500:
		print ("found", n)
		break