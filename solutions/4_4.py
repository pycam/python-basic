import subprocess

output = subprocess.check_output(['ls'])

filenames = output.split("\n")

for filename in filenames:
    if filename.endswith(".py"):
        print filename.upper()

# using inbuilt listdir() from python
import os
for f in os.listdir('.'):
    if f.endswith('.py'):
        print f.upper()
