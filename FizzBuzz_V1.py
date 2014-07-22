#This is the FizzBuzz project with the numbers hard coded

for i in range (1, 101):
	if ((i % 3 == 0) and (i % 5 == 0)):
		print "%d " % (i) + "FizzBuzz \n"
	elif (i % 3 == 0):
		print "%d " % (i) + "Fizz \n" 
	elif (i % 5 == 0):
		print "%d  "% (i) + "Buzz \n"
	else:
		print "%d \n" % (i)
