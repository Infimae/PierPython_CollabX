hrs = input("Enter Hours:")
h = float(hrs)
rate = 10.50
o=0
#Setup program to calculate overtime pay, if any.

if h>=40:
	o = h%40
	pay = rate*40+rate*1.5*o
else:
    pay = h*rate
    
print(pay)