n=int(input("Enter a number:"))
m=int(input("How many multiples:"))
i = 1
while i<m:
    sum = n * i
    print(n,"x",i, "=",sum)
    i = i +1