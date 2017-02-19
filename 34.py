import math
nums = []
for i in range(3,1000000):
	if (sum([math.factorial(int(c)) for c in str(i)]) == i):
		nums.append(i)

print(sum(nums))