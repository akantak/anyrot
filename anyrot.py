# polish lowercase alphabet as an example

alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
numbers_dict = {i:alphabet[i] for i in range(len(alphabet))}
letters_dict = {alphabet[i]:i for i in range(len(alphabet))}

def rot(rotation_factor:int, text_to_rot:str):
    new_text = ""
    for letter in text_to_rot:
        if letter not in alphabet:
            new_text += letter
            continue
        no = (letters_dict[letter] + rotation_factor) % len(alphabet)
        new_text += numbers_dict[no]
    return new_text

sample_rotated_text = "ółu, ło uł ążncęćjq, ł ei ążńjigłu"

# show all possible values
for x in range(len(alphabet)):
    rot(x, sample_rotated_text)
