import sys

print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} arguments at run time".format(len(sys.argv))

if len(sys.argv) > 1 and sys.argv[1] != None:
	if sys.argv[1] <100:
		end = sys.argv[1]
	else:
		end = 100
else:
	endnum = int(raw_input("What Number Shall we Count To?"))
	if endnum <100:
		end = endume
	else: end = 100

print "Jaime's FizzBuzz counting up to",end


def zerorem(onenum,twonum):
	result == onenum%twonum
	if result == 0:
		return True
	else:
		return False

def fizzbuzzy():
	for number in range(0,end+1):
		if zerorem(number,15):
			print "FizzBuzz"
		elif zerorem(number,3):
			print "Fizz"
		elif zerorem(number,5):
			print "Buzz"
		else:
			print number








