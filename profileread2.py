f = open("profile.txt", "r")
f.seek(26)
line = f.readline()
print(line)
f.close()
