end = int(raw_input("What Number Shall we Count To?"))

list = range(0,end+1)

print "Jaime's FizzBuzz counting up to",end

for number in list:
	if number%3 == 0 and number%5 == 0:
		print "FizzBuzz"
	elif number%3 == 0:
		print "Fizz"
	elif number%5 == 0:
		print "Buzz"
	else:
		print number



