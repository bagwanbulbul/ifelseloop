num = 1
while (num<100):
	if (num%3 == 0):
		print "nav"
	elif (num%7 == 0):
		print "gurukul"

	elif (num%3==0 and num%7==0):
		print "navgurukul"
	else:
		print num
	num = num+1
