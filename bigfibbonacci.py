fibbonacci = [1,2]
total = 0;
while (True):
	fibbonacci.append(fibbonacci[-1] + fibbonacci [-2])
	if (len(str(fibbonacci[-1])) >= 1000):
		break;




print(len(fibbonacci))