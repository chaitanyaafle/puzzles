#!/usr/bin/env python3

import json

def check_guess(word_bank, input_word, guess_list):
    out = []
    guess = None
    while not guess:
        guess = input("Input your 5 letter guess word:\n")
        if guess not in word_bank:
            print("Invalid word.")
            guess = None
            continue
        elif guess in guess_list:
            print("You've already guessed '{}' before. Guess something else.".format(guess))
            guess = None
            continue
        else:
            for jj in range(5):
                if input_word[jj]==guess[jj]:
                    out.append('*')
                elif guess[jj] in input_word:
                    out.append('!')
                else:
                    out.append('x')
    print(out)
    guess_list.append(guess)
    return out, guess_list

word_bank = json.load(open("../data/english-words/words_dictionary.json"))

possible_words = [word for word in word_bank if len(word)==5]

input_word = 'ghost'

guess_list = []
win = False
for jj in range(6):
    check, guess_list = check_guess(word_bank, input_word, guess_list)

    if check == ['*', '*', '*', '*', '*']:
        win = True
        print("You guessed the word correctly! Hurray! :)")
        break
if not win:
    print("Bummer! You've used all of your 6 tries. The correct word was '{}'".format(input_word))
