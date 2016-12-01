# Create a string variable with your full name
name = "Boris Johnson"

# Split the string into a list
names = name.split(" ")

# Print out your surname
surname = names[-1]
print("Surname:", surname)

# Check if your surname contains the letter 'e'
pos = surname.find("e")
print("Position of 'e':", pos)

# or contains the letter 'o'
pos = surname.find("o")
print("Position of 'o':", pos)

### Optional --------------------------------------------------------

# Use a format string to print out your first name and the length of your first name
print("%s is %d characters long" % (names[0], len(names[0])))
