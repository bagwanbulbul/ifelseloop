#input the temperature by user
temp = int(raw_input("enter your number"))
# temperature if less than 0
if temp < 0:
	print "freezing"
#temperature is greater than 0 and less than 11
elif temp > 0 and temp < 11:
	print "vary cold"
#temperature is greater than 11 and less than 20
elif temp > 11 and temp < 20:
	print "cold water"
#temperature is greaer than 20 and less than 30
elif temp > 20 and temp < 30:
	print "normal water"
#tempreture is greater than 30 and less than 40
elif temp > 30 and temp < 40:
	print "its hot"
#temperature is greater than equal to 40
elif temp >= 40:
	print "its too much hot"
else:
	print "nothing"
