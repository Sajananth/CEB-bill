# Solution to Calculate the Domestic use of Electricity Tarrif
# https://ceb.lk/commercial-tariff/en
# Domestic use is taken for the purpose of learning
# Assumed that the consumption will be higher than 2 units per day

# Assign Variables
units = int(input("Enter the No. of Units Consumed : "))
days = int(input("Enter the No. of Days of Reading : "))
slot = 0

# Calculate the Required No. of Slots

if units / days > 6:
	slot = 7
else:
	reminder = units % days
	if reminder == 0:
		slot = units / days
	else:
		unit = units - reminder
		slot = (unit / days) + 1

slot = int(slot)
# DYNAMIC ASSIGNMENT OF VALUES TO ARRAY

# Empty List (Array)
slots = []

# Assigning values to array. Note, we assign up to slot size - 1
for i in range(0,slot-1):
	slots.append(days)
	units = units - days

# For the last slot, we assign the balance units
slots.append(units)

# Cost of Each Unit Consumption
unitCost = [7.85,7.85,10,27.75,32,32,45]

# Calculating the Cost of Consumption
costOfUse = 0 
for j in range(0,slot):
	costOfUse = costOfUse + (slots[j] * unitCost[j])

# Calculating the Fixed Cost
fixedCosts = [30,60,90,480,480,480,540]
fixedCost = fixedCosts[slot-1]

# Calculating the Total Cost for the Month
totalCost = costOfUse + fixedCost

# Output the Values
print ()
print ("----- ELECTRICITY USAGE -----")
print ("Fixed Cost is Rs.",fixedCost)
print ("Cost of Consumption is Rs.",costOfUse)
print ("Total Cost is Rs.", totalCost)

# END OF PROGRAMME