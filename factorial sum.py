def factorial(factor):
	if (factor != 1):
		return (factor * factorial(factor-1));
	else:
		return (1);

num = factorial(100)
a = list(str(factorial(100)))
a = [int(i) for i in a]
print(sum(a))