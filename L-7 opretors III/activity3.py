print("Enter your 5 marks:")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
totalmarks=mark1+mark2+mark3+mark4+mark5
avg=(totalmarks)/5
if avg>=90:
    print("grade A")
elif avg>=80:
    print("grade B")
elif avg>=70:
    print("grade C")
elif avg>=60:
    print("grade D")
else:
    print("grade F")
