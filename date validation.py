d = int(input("ENTER THE DATE:"))
m = int(input("ENTER THE MONTH:"))

if 0 < d < 32:
    if 0 < m < 13:
        print("Valide date")
else:
    print("Invallid date")