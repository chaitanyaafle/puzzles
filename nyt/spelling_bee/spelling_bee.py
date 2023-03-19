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
letters = args.letters

letters.append(cl)

# Check if there are a total of 7 letters
if len(letters)!=7:
    raise ValueError("Please pass six letters and a central letter")

# Check if there are nop duplicates:
if len(letters) != len(set(letters)):
    raise ValueError("Duplicate letters are not allowed")

word_bank = json.load(open("../data/english-words/words_dictionary.json"))
