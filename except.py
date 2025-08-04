#Exception handling

try:
    num = int(input("Enter a number"))
    print(1 / num)
except ZeroDivisionError:
    print("You cannot divide by Zero Great person")
except TypeError:
    print("Type Error")
except ValueError:
    print("value Error")
finally:
    print("Do some Clean up here")



