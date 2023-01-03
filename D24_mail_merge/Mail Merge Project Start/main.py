# Read names
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    generic_letter = file.read()

for name in names:
    name_stripped = name.strip()
    letter = generic_letter.replace("[name]", name_stripped)
    # Write txt file
    with open(
        f"/Users/nicolas/git/100-days-of-Python/D24/Mail Merge Project Start/Output/ReadyToSend/letter_to_{name_stripped}.txt",
        mode="w",
    ) as file:
        file.write(letter)
