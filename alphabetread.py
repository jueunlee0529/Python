f = open("alphabet.txt", "r")
index = int(input("index : "))
line = f.readline()
f.seek(index)
print("%s" % (f.read()))
