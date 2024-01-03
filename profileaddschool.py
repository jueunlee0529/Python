f = open("profile.txt", "a")
school = input("School : ")
f.write("School : %s\n" % school)
f.close()
