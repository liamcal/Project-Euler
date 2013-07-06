def isPal(number):
	if len(number) < 2:
		return True
	elif number[0] == number[-1]:
		return (isPal(number[1:-1]))
	else:
		return False


largest = 0;

for i in reversed(range(999)):
	for j in reversed(range(999)):
		tot = i*j
		if (isPal(str(tot)) and tot > largest):
			largest = tot;
			print (tot, "Is pal")
			break;