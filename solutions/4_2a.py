data = [2,4,6,8,10]

with open("numbers.txt", "w") as out_file:
    for d in data:
        out_file.write(str(d)+"\n")



