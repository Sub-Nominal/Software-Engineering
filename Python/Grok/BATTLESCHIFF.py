hit = []
att = []
while True:
    guess = input('Guess: ')
    if guess == "":
        break
    att.append(guess)
    if guess in hit:
        print("You've chosen that square already")
    else:
        hit.append(guess)
        print(f'Hit {guess}')
    