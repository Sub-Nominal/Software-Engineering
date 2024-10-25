
counts = {}
line = input('Line: ')
while line:
    words = line.lower().split()
    for i in range(len(words) - 1):
      bigram = (words[i], words[i + 1])
      counts[bigram] = counts.get(bigram, 0) + 1
    line = input('Line: ')

for bigram in counts:
   freq = counts[bigram]
   if freq > 1:
     print(' '.join(bigram) + ':', freq)