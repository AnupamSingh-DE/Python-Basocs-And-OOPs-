#list comprehension

double = []

for x in range(1,11):
    double.append(x*2)


print(double)

triples = [ x * 3 for x in range(1,11)]

print(triples)

squares = [pow(x,2) for x in range(1,21)]
print(squares)