#given number 
number = 1
while number<25:
	if (number%2 == 1):
		print "wired ",number
	elif (number%2==0 and 2<5):
		print "not wired",number
	elif (number%2 == 0 and 6<20):
		print "little wired",number
	elif (number%2==0 and 20<=25):
		print "full wired",number
	number = number+1
