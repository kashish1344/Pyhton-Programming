def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    return z1,z2,z3,z4
x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
#print(calc(x,y))

#(THEY ARE CALLED PACKING AND UNPACKING)
# a = calc(x,y)
#a,b,*c = calc(x,y)

a,b,c,d = calc(x,y)
print("Sum is ",a)
