h = float(input("enter the no of hours ="))
r = float(input("enter the rate per hour ="))
def computepay():  
    if h<=40:
        print("Pay",h*r)
        return h*r
    else:
        hr=h-40
        print("Pay",(40*r)+(hr*r*1.5))
        return (40*r)+(hr*r*1.5)
computepay() 