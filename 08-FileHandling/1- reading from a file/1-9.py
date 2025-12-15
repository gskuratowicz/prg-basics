###
# Prints employees employed in a specified position.
#

# Employee List
file = 'it_company.txt'

# Position
job_title = 'Software Engineer'

def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file(file)
file_lines = file_content.splitlines()

i = 1
for line in file_lines:
   if job_title in line:
      print (f"{i}. {line}")
      i += 1