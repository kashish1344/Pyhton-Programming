def atm():
    total=10000
    pin=input("Enter Your Pin: ")
    assert (pin=='12345'),'Login Faild'
    print("Log in Success")

    amount= int(input("Enter the Amount :"))
    assert (amount>total),'Insufficient Error '
    total-=amount
    print("Remaining Balnace  is : ",total)

try:
    atm()
except AssertionError as err:
    print(err)