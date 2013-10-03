import subprocess

output = subprocess.check_output(["ls *.py"], shell=True)

filenames = output.split("\n")

for filename in filenames:
    #if filename.endswith(".py"):
    print filename.upper()

