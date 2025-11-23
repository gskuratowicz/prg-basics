###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters: ', movie.upper())

# print title in small letters
print('Title in lowercase letters: ', movie.lower())

# print how many times the vowel "e" appears in the title
print(f'The vowel "e" appears {movie.count('e')} times in the title.')

# print where in the text is the word "Lord"
print(f'The word "Lord" is at index {movie.find('Lord')}.')
# print where in the text is the word "dragon"
print(f'The word "dragon" is at index {movie.find('dragon')}.')