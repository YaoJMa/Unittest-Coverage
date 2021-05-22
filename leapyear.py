def leapCalc():
	#Asks user for input for year
	year = input("Enter a year: ")
	#Checks conditions to see if user input is leap year
	if(year.isdigit() == True):
		if(int(year) %4 == 0 and int(year) %100 != 0 or int(year) %400 == 0):
			print("It is a leap year") 
		else: 
			print("It is not a leap year")
	#Error checking for if user does not enter a int
	else:
		print("Please enter a digit for years")

leapCalc() 
	
