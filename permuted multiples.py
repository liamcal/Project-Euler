import timeit
runtimes=[]
for i in range(100):
	start = timeit.default_timer()

	([i for i in range(123456,166666) if all(set(str(a*i)) == set(str(i)) for a in range(1,7)) ][0])
	#for i in range(123456,166666):
	#	if all(set(str(a*i)) == set(str(i)) for a in range(1,7)):
	#		#print(i)
	#		break
	stop = timeit.default_timer()

	runtimes.append(stop - start)
print(sum(runtimes)/len(runtimes))
#print([ifor i in range(123456,166666) if all(set(str(a*i)) == set(str(i)) for a in range(1,7)) ][0])

