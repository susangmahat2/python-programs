Amount=int(input("Enter the amount :"))
Note1=Amount//100
Note2=(Amount%100)//50
Note3=((Amount%100)%50)//10
print("note of 100RS",Note1)
print("note of 50RS",Note2)
print("note of 10RS",Note3)
