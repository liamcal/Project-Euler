def primes(limit):
    a = [True] * limit                          
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     
                a[n] = False


primes = set(primes(800000))
trunc=set()
for n in primes:
	s=str(n)
	if (s[0] == '3' or s[0] == '2' or s[0] == '5' or s[0] == '7') and (s[-1] == '3' or s[-1] =='7' )and len(s)>1 :
		if all(int(s[i:]) in primes and int(s[:-i]) in primes for i  in range(1,len(s))):
			trunc.add(n)
		if len(trunc) > 10:
			break
print(sum(trunc))
