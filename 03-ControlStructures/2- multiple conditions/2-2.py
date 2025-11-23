###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S' or 's':
    print('S: Small size')
elif size == 'M' or 'm':
    print('M: Medium size')
elif size == 'L' or 'l':
    print('L: Large size')
elif size == 'XL' or 'xl':
    print('XL: Extra large size')
else:
    print('thats not a size brochacho')