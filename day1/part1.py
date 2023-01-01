import sys
import os

input_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(sys.path[0], "test.txt")
print(f"Reading file named {input_file}")
file1 = open(input_file, 'r')
Lines = file1.readlines()
  
answer = 0
elf=0
for line in Lines:
    if line.isspace() :
        answer=max(elf,answer)
        elf=0
    else:
        elf=elf+int(line)

    

print(f"answer={answer}")
