###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char != " ":
        letter_code = ord(char)
        encrypted_letter_code = letter_code + 1
        encrypted_letter = chr(encrypted_letter_code)
    else: print(char)
    encrypted_text = encrypted_text + encrypted_letter



print('The message before encryption is: ', plain_text)
print('The message after encryption is: ', encrypted_text)