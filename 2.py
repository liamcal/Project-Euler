fibbonacci = [1,2]
total = 0;
while (True):
	fibbonacci.append(fibbonacci[-1] + fibbonacci [-2])
	if fibbonacci[-1] > 4000000:
		fibbonacci.pop()
		break;

for i in fibbonacci:
	if i % 2 == 0:
		total += i

print(total)