weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))
bmi=weight/(height**2)
print("Your BMI is:",bmi)
if bmi<18.5:
    print ("you're underweight")
elif bmi<24.9:
    print("you're normal weight")
elif bmi<29.9:
    print("you're overweight")
else:
    print("you're obese")
