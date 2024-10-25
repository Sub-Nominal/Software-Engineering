word = input('Word to look for: ')
word = word.lower()
w = False
with open('book.txt') as f:
    for line in f:
        if word in line.lower():
            print(f"{word} was found in the book.")
            w = True
            break
    if w == False:
        print(f"{word} was not found in the book.")