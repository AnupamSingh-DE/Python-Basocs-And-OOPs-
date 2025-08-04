#here iam to make 2d list

groceries = [["apple","banana","pinapple"],
             ["Sampoo","soap"],
             ["garam masala", "sabji masala","samber masala"]]

for collection in groceries:
    for items in collection:
        print(items.upper(), end = ", ")

    print()

print("You are doing great Anupam")