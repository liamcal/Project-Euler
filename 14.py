def collatz(start):
	n = start
	seq = []
	seq.append(int(n))
	while n > 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		seq.append(int(n))
	return(seq)

m = 0
t = 0
for i in range(1000000):
	if len(collatz(i)) > m:
		m = len(collatz(i))
		t=i
		print ("new max",m,'term',t)
print(t) 