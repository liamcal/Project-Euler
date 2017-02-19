from functools import reduce
numerators = []
denominators = []
for d in range (10,100):
	for n in range(10,d):
		ds = set(str(d))
		ns = set(str(n))
		c = list(ns.intersection(ds))
		if c and c[0] != '0':
			dl = list(str(d))
			nl = list(str(n))
			nl.remove(c[0])
			dl.remove(c[0])
			d2 = int("".join(dl))
			n2 = int("".join(nl))
			try:
				if n/d == n2/d2:
					print(n,d,n2,d2, "found")
					numerators.append(n2)
					denominators.append(d2)
			except ZeroDivisionError:
				pass
ntot = reduce(lambda x, y: x * y, numerators)
dtot = reduce(lambda x, y: x * y, denominators)
print(ntot,'/',dtot)