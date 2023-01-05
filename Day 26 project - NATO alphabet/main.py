""" Reads a csv file which contains a code name for each letter, converts the data to a dictionary,
    asks the user for an input and prints the code name for each letter in the input"""

import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dic = {row.letter: row.code for index, row in alphabet.iterrows()}

s = input("Please enter a word\n")
code_names = [alphabet_dic[c.upper()] for word in s.split() for c in word]
print(code_names)
