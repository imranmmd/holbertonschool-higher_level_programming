#!/usr/bin/python3
s = ''
for i in range(97, 97+26):
    if i == 113 or i == 101:
        continue
    s = s + chr(i)
print("{}".format(s), end="")
