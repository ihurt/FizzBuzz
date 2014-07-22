#This is the FizzBuzz project with user inputting in a numbers
user_input = raw_input("Please input a number between 1 and 100? ")
for i in range (1, (int(user_input) + 1)):
	if ((i % 3 == 0) and (i % 5 == 0)):
		print "%d " % (i) + "FizzBuzz \n"
	elif (i % 3 == 0):
		print "%d " % (i) + "Fizz \n" 
	elif (i % 5 == 0):
		print "%d  "% (i) + "Buzz \n"
	else:
		print "%d \n" % (i)
