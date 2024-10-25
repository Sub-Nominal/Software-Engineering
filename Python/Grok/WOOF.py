f = open("Fixed.txt", "w")
s = open('letter.txt')
for line in s:
    if not line.startswith("WOOF!"):
        f.write(line)
f.close()
s.close()