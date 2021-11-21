def atm():
    total=10000
    pin=input("Enter Your Pin: ")
    if pin=='12345':
        print("Login Success")
    else:
        raise ValueError("Login Failed")


    amount= int(input("Enter the Amount :"))
    if amount>total:
        raise ValueError("Insufficient Error ")
    else:
        total-=amount
        print("Remaining Balnace  is : ",total)

try:
    atm()
except ValueError as err:
    print(err)