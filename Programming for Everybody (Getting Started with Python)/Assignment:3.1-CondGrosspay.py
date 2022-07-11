hours = float(input("Enter the no of hours = "))
rph = float(input("Enter the rate per hour ="))
if hours <= 40:
    print(hours*rph)
else:
    hour = hours-40
    print((40*rph)+(hour*rph*1.5))