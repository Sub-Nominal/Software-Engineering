msg = input('Message? ')
decoded = msg[0]
for i in range(3, len(msg), 3):
    decoded += ' ' + msg[i]
print(decoded)