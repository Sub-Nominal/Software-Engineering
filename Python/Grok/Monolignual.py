'''eng = ['english', 'ENGLISH', 'English']
br = False
def ip(c = 1):
    while True:
        l = input('Line: ')
        if l == " ":
            br = True
            return br
        if c == 1:
            c = c +1
            engline = l
            return engline
        else:
            return l

def diff(engline, l):
    engline = engline - l
    if engline != 0:
        print(f"{engline} is monolingual")
    else:
        print('Everyone is multilingual!')

while br == False:
    ip()
else:
    while br == True:
        diff()'''

monolingual = None

line = input('Line: ')
while line:
  line = line.split()
  names = set(line[1:])
  if monolingual is None:
    monolingual = names
  else:
    monolingual -= names
  line = input('Line: ')

if monolingual:
  for name in monolingual:
    print(name, 'is monolingual.')
else:
  print('Everyone is multilingual!')


