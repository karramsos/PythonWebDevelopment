balance =  1000
rate = 1.02
years = 0
while balance < 5000:
	balance *= rate
	years += 1
print "It takes " + str(years) + " years to reach $5000."
