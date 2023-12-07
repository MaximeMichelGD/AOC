test = set()

for i in range(10000):
    test.add(i)

for j in range(5000):
    test.add(j)

print(len(test))