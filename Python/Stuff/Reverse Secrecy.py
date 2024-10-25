msg = input('Line: ')
newmsg = msg[::-1]
decoded = newmsg[0]
for i in range(3, len(newmsg), 3):
    decoded += ' ' + newmsg[i]
print(decoded)