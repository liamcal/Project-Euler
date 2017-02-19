

divisors = [i for i in range(11,21)]

test = 20
while True:
	if all( (test % i == 0) for i in divisors):
		print ("Found: ", test)
		break
	test += 20;
