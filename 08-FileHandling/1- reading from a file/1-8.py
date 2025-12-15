###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

# calculates the number of words in a line
sum = 0
for line in file_lines:
   split_file_line = line.split()
   number_of_words = len(split_file_line)
   sum += number_of_words

print(file_content)
print('Total number of words in text: ', sum)
