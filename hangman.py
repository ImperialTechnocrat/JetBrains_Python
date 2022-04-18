import random


def select_word():
    random.seed()
    words = ["python", "java", "swift", "javascript"]
    word = random.choice(words)
    return word


def cover_word(word, letters):
    cover = []
    for i in word:
        if i in letters:
            cover.append(i)
        else:
            cover.append('-')
    return ''.join(cover)


def is_there(word, letter):
    if letter in word:
        return 1
    return 0


def game_control():
    word = select_word()
    attempts = 8
    correct = []
    incorrect = []
    while attempts > 0 and len(correct) != len(set(word)):
        cover = cover_word(word, correct)
        print()
        print(cover)
        guess = input("Input a letter:")
        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        if guess.isupper() or not guess.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if guess in correct or guess in incorrect:
            print("You've already guessed this letter.")
            continue
        if guess in correct:
            print("No improvements.")
            attempts -= 1
        elif is_there(word, guess):
            correct.append(guess)
        else:
            print("That letter doesn't appear in the word.")
            incorrect.append(guess)
            attempts -= 1
    if attempts != 0:
        print(f"""
You guessed the word {word}!
You survived!""")
        return 1
    else:
        print("You lost!")
        return 0


print("H A N G M A N")
won = 0
lost = 0
while True:
    select = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if select == 'play':
        if game_control():
            won += 1
        else:
            lost += 1
    elif select == 'results':
        print(f"You won: {won} times.")
        print(f"You lost: {lost} times.")
        continue
    elif select == 'exit':
        break
