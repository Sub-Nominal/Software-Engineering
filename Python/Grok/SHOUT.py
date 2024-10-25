f = open('orders.txt')
for line in f:
    line = line.strip()
    line= line.upper()
    print(line)