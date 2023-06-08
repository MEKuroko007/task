#!/usr/bin/python3
import os
filename=str(input("filename : "))
command=str(input("command : "))
comment=str(input("comment : "))
content=f"#!/bin/bash\n{command}\n"

with open(filename,"w") as f:
    f.write(content)

os.chmod(filename,0o700)
print("Done!")
print(40*"-")
os.system(f'cat {filename}')
print(40*"-")
os.system('git add . ')
os.system(f'git commit -m "{comment}" ')
os.system('git push')
print("happy hacking")
