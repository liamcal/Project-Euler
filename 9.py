import math
product = 0
for i in range(1,1000):
	for j in range(1,1000):
		total = math.sqrt(i*i + j*j)
		if total + i + j == 1000:
			print ("a: ",i, "b: ", j, "c: ",total)
			product = i*j*total
print (product)