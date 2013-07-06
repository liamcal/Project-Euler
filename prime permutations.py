import itertools
j = lambda x:(''.join(str(i) for i in x))
def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True
        primes.append(i)
    return primes
primes = set([p for p in primes_sieve(10000) if p >= 1000])
l = [sorted(set([int(j(perm)) for perm in(itertools.permutations([int(d) for d in str(p)]))]).intersection(primes))  for p in primes ]
answers =[]
for s in l:
	while len(s) > 0 :
		n1 = s.pop(0)
		for n in s:
			n2 = n
			n3 = n2 + abs(n2-n1)
			if len(set(s).intersection(set([n3]))) == 1 and all([n1,n2,n3] != s for s in answers)				:
				answers.append([n1,n2,n3])
print(answers)