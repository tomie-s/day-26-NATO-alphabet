import pandas

# TODO 1. Create a dictionary in this format
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def create_nato_word():
    word = input('Enter a word: ').upper()
    try:
        nato_word_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print('Please only enter letters in the alphabet')
        create_nato_word()
    else:
        print(nato_word_list)


create_nato_word()
