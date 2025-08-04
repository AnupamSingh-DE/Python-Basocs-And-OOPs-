#testing function

# def create_name(first,last):
#     first = first.upper()
#     last = last.upper()
#     return first+ " " +last
#
# full_name = create_name("Anupam","Singh")
#
# print(full_name)

import time

def count(start : 0 , end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)

    print("Doing great")

#num1 = int(input("Enter starting"))
num2 = int(input("Enter ending"))
count(num2)