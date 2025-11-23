###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    
    # add one to the character's code
    if ord(char) != 32:
        letter_code = ord(char)
        encrypted_letter_code = letter_code + 1
    else:
        letter_code = ord(char)
        encrypted_letter_code = letter_code
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_letter = chr(encrypted_letter_code)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + encrypted_letter



print(f'The message before encryption is: {plain_text}')
print(f'The message after encryption is: {encrypted_text}')