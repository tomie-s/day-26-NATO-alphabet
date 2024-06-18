import pandas

# TODO 1. Create a dictionary in this format
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ').upper()
nato_word_list = [nato_dict[letter] for letter in word]

print(nato_word_list)
