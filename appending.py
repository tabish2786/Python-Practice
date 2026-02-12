L = [1, 2, 2, 3, 4, 4, 5, 6,2,3,8,23,98,4]

new = []

for x in L:
    if x not in new:
        new.append(x)
print(new)