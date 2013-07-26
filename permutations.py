import itertools
c = lambda x:int(''.join(str(i) for i in x))
i = lambda x: int(x)
d = [2,3,5,7,11,13,17]
pandigitals = (sorted(list(itertools.permutations([i for i in range(10)]))))
ans = []
for t in pandigitals:
	p = c(t)
	try:
		if all(i(p[n+1:n+4]) % d[n] == 0 for n in range(7)):
			ans.append(i(p))
			print("found" , i(p) )
	except IndexError:
		print("Error on ", t)
print(ans)
