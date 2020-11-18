import pandas

alphabets = pandas.read_csv("data/nato_phonetic_alphabet.csv")

alphabets_dict = {row.letter: row.code for (index, row) in alphabets.iterrows()}
name = input("Enter your name:  ")
result = []
for letter in name:
    result.append(alphabets_dict[letter.upper()])

print(result)
