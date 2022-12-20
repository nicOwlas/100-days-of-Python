import pandas

student_data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
NATO_dic = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Write a word. It will be spelled in the NATO dictionnary: ")

NATO_spelling = [NATO_dic[letter.upper()] for letter in word]
print(NATO_spelling)
