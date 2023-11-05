import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

name = input("Enter your name?:").upper()

new_dict = {row.letter:row.code for (index, row) in df.iterrows()}
output_list  = [new_dict[letter] for letter in name]
print(output_list)
