name = "Boris Johnson"
names = name.split(" ")

surname = names[-1]
print "Surname:", surname

pos = surname.find("e")
print "Position of 'e':", pos

pos = surname.find("o")
print "Position of 'o':", pos

format_string = "%s is %d characters long"

print format_string % (names[0], len(names[0]))
