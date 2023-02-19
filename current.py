unit=float(input("enter the number of unit:"))
noOfDays=float(input("enter the day:"))
if unit<=noOfDays:
	cost=float(7.85*unit)
elif unit<= 2*noOfDays:
	cost=float(7.85*unit)
elif unit<=3*noOfDays:
	noOfDay=unit-2*noOfDays
	cost=float(7.85*(2*noOfDays)+10*noOfDay)
elif unit<=4*noOfDays:
	noOfDay=unit-3*noOfDays
	cost=float(7.85*(2*noOfDays)+10*noOfDays+27.75*noOfDay)
elif unit<=6*noOfDays:
	noOfDay=unit-4*noOfDays
	cost=float(7.85*(2*noOfDays)+10*noOfDays+27.75*noOfDays+32*noOfDay)
else:
	noOfDay=unit-6*noOfDays
	cost=float(7.85*(2*noOfDays)+10*noOfDays+27.75*noOfDays+32*(2*noOfDays)+45*noOfDay)


if unit<=60:
	fixedPrice=0
elif unit<=90:
	fixedPrice=90
elif unit<=180:
	fixedPrice=480
else:
	fixedPrice=540
totalCost=cost+fixedPrice
print("total cost:",totalCost,"rs")
