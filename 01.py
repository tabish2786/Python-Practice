f = open("poem.txt")
content = f.read()
if("IRONMAN" in content):
    print("The word IRONMAN is present in the content")

else:
    print("The word IRONMAN is not present in the content")

f.close()