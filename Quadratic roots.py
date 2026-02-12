a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b*b - 4*a*c

r1 = (-b + d**0.5) / (2*a)
r2 = (-b - d**0.5) / (2*a)

print("Root 1 =", r1)
print("Root 2 =", r2)