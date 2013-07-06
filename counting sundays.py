

date = input("Enter the date in the form dd,mm,yyyy: ")
while date:
	monthlengths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	days = {0: "Sunday", 1: "Monday",2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5:"Friday", 6:"Saturday"}
	months = {1: "January", 2: "February", 3:"March",4: "April", 5: "May", 6:"June",7: "July", 8: "August", 9:"Septimeber",10: "October", 11: "November", 12:"December" }
	day = 2
	curday = 1
	curmonth = 1
	monthdays = 0
	curyear = 1901
	firstsuns = []
	date = (date.split(','))
	date = [int(date[i]) for i in range(len(date))]
	print ("Date entered was", months[date[1]], date[0], date[2])
	while (curday != date[0] or curmonth != date[1] or curyear != date[2]):
		if curyear % 4 == 0 and (not curyear % 100 == 0 or curyear % 400 == 0 ) and curmonth == 2:
			monthdays = 29
		else:
			monthdays = monthlengths[curmonth]

		if curday == monthdays:
			curday = 1
			if curmonth == 12:
				curmonth = 1
				curyear += 1
	#			print("New year", curyear, "Currently", firstsuns)
			else:
				curmonth += 1
	#		print ("New Month", curmonth)
		else:
			curday += 1
	#	print(curday, curmonth, curyear)
		day = (day + 1) % 7

	print ("Date entered was a",days[day])
	date = input("Enter the date in the form dd,mm,yyyy: ")

