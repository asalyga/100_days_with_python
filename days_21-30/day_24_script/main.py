import pandas as pd

# TODO 1. Create a dictionary:
nato_dic = pd.read_csv("nato_phonetic_alphabet.csv",
                       index_col=0,
                       header=None,
                       squeeze=True).to_dict()
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_name = input("Please Type The word: ").upper()

user_word_nato = [nato_dic[letter] for letter in word_name]
print(user_word_nato)
