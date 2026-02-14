x=5
if(type(x)is int):
    print("true")
else:
    print("false")

y=3.5
if(type(y) is float):
    print("true")
else:
    print("false")

x=20
y=20
if(x is y):
    print("x & y are same identity")
else:
    print("x & y are different identity")
y=30
if(x is not y):
    print("x & y are different identity")
