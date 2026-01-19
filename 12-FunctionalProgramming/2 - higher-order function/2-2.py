names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

sort_names = lambda names : sorted(names,key=len)

print(sort_names(names))