try:
    a = int(input("Enter Your First Number: "))
    b = int(input("Enter Your Second Number: "))

    c = a + b
    print("Sum is: " , c)

    d = a - b
    print("Sub is: " , d)

    e = a * b
    print("Mulplication is: " , e)

    f = a / b
    print("Divsion is: " , f)

except ZeroDivisionError as err:
    print("Cannot Divisible by Zero")
except ValueError as errr:
    print("Invalid Input")
except BaseException as exp:
    print("Error...",exp)