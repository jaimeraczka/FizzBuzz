print "Jaime's FizzBuzz counting up to 100!"

list = range(101)

for number in list:
	if number%3 == 0 and number%5 == 0:
		print "FizzBuzz"
	elif number%3 == 0:
		print "Fizz"
	elif number%5 == 0:
		print "Buzz"
	else:
		print number



