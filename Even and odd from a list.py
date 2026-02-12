L= [2,19,24,56,77,59,90,62,46]

even = []
odd = []
for x in L:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)