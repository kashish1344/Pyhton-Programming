a=int(input("Enter Marks in 1st Subject: "))
b=int(input("Enter Marks in 2nd Subject: "))
c=int(input("Enter Marks in 3rd Subject: "))
d=int(input("Enter Marks in 4th Subject: "))
e=int(input("Enter Marks in 5th Subject: "))
total=a+b+c+d+e
percent=(total/500)*100
print("Total Marks=",total,"Percentage= ",percent)
if percent>=80:
    print("Your Grade is 'A' ")
elif percent>=60:
    print("Your Grade is 'B' ")
elif percent>=40:
    print("Your grade is 'C' ")
else:
    print("Yourn Grade is 'D' ")
