###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char != ' ':
        encrypted_code = ord(char) + 1
        new_letter_code = chr(encrypted_code)
    else:
        new_letter_code = char
    encrypted_text += new_letter_code

print(plain_text)
print(encrypted_text)