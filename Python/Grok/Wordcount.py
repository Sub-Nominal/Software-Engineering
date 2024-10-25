all = []
occurrence = {}
while True:
    line = input('Enter line: ')
    if not line:
        break
    word = line.split()
    for w in word:
        if w in occurrence:
            occurrence[w] +=1
        else:
            occurrence[w]=1
for word in sorted(occurrence):
    print(word, occurrence[word])