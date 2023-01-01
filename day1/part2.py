import sys
import os

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(sys.path[0], "test.txt")
print(f"Reading file named {input_file}")
file1 = open(input_file, 'r')

Lines = file1.readlines()
  
elves = []
elf=0
for line in Lines:
    if line.isspace() :
        elves.append(elf)
        elf=0
    else:
        elf=elf+int(line)
    

elves.sort()
elves.reverse()

answer=elves[0]+elves[1]+elves[2]
print(f"answer={answer}")
