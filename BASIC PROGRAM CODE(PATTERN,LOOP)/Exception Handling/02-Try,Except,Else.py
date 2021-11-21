try:
    a = int(input("Enter Your First Number: "))
    b = int(input("Enter Your Second Number: "))
    c = a + b
    d = a - b
    e = a * b
    f = a / b


except ZeroDivisionError as err:
    print("Cannot Divisible by Zero")
except ValueError as errr:
    print("Invalid Input")
except BaseException as exp:
    print("Error...",exp)

else:
    print("Sum is: ", c)
    print("Mulplication is: ", e)
    print("Divsion is: ", f)
    print("Sub is: ", d)
