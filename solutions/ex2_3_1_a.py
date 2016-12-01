# Script that writes the values of a list of numbers to a file,
# with each number on a seperate line.

data = [2, 4, 6, 8, 10]

with open("numbers.txt", "w") as f:
    for d in data:
        f.write(str(d) + "\n")
