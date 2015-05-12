data = [2, 4, 6, 8, 10]

with open("numbers.txt", "w") as f:
    for d in data:
        f.write("%s\n" % d)
