import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:

NATO_DICT={row.letter: row.code for (index, row) in data.iterrows()}
#print(NATO_DICT)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output = [NATO_DICT[letter] for letter in word]
print(output)
