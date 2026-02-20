units=int(input("Enter the number of units consumed:"))
if units<=50:
    amount=units*2.60
    tax=25
elif units<=100:
    amount=130+(units*3.25)
    tax=35
elif units<=200:
    amount=130+162.50+((units-100)*5.26)
    tax=45
else:
    amount=130+162.50+526+((units-200)*7.87)
    tax=45
total=amount+tax
print("the total amount to be paid is:",total)
