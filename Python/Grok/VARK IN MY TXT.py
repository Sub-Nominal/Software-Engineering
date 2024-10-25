f = open('vark.txt').read().lower()
f = f.split("\n")
word = "Aardvark"
word = word.lower()
for index, line in enumerate(f):
    a = line.count("a")
    r = line.count("r")
    d = line.count("d")
    v = line.count("v")
    k = line.count("k")
    if a >=3 and r>=2 and d>=1 and v>=1 and  k>=1:
        print(f'Aardvark on line {index+1}')