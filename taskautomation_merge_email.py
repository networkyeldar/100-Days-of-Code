PLACEHOLDER = "[name]"
with open("./names/names.txt") as invited_names:
    names = invited_names.readlines()

with open("./letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/voevoda/Desktop/my folder/python learning/letter_to_{stripped_name}.txt",mode="w") as created_letter:
            created_letter.write(new_letter)
