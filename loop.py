#hey iam here to test loops
#printing rectangle

# row = int(input("Enter rows"))
# columns = int(input("Enter columns"))
#
# for i in range(row):
#     for j in range(columns):
#         print(j,end = " ")
#         print("")

length = int(input("Enter length"))
breadth = int(input("Enter breadth"))

for i in range(breadth):
    for j in range(length):
        print("$", end = " ")

    print()
