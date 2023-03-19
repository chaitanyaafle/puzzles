#!/usr/bin/env python3

import argparse
import json

parser = argparse.ArgumentParser(description='Solve NYT spelling bee')
parser.add_argument('--central_letter', type=str,
                    help='The central alphabet which has to be a part of any word', required=True)
parser.add_argument('--l', '--letters', nargs=6, type=str, required=True,
                    help='The other six letters)')

args = parser.parse_args()
cl = args.central_letter
letters = args.l

letters.append(cl)

# Check if there are a total of 7 letters
if len(letters)!=7:
    raise ValueError("Please pass six letters and a central letter")

# Check if there are nop duplicates:
if len(letters) != len(set(letters)):
    raise ValueError("Duplicate letters are not allowed")

word_bank = json.load(open("../data/english-words/words_dictionary.json"))

solutions = []

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

unacceptable_letters = [letter for letter in alphabet if letter not in letters]

# eliminate short words
possible_words = [word for word in word_bank if len(word) > 3]

# assert that the central letter must appear in the word
possible_words = [word for word in possible_words if cl in word]

#cond = if any(l in unacceptable_letters )
possible_words = [word for word in possible_words if any(l in unacceptable_letters for l in word) == False]

print(possible_words)
