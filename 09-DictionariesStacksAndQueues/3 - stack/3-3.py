import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct


def brackets_ok(expression):
    stack = queue.LifoQueue()
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression: # analyzes every chracter in expression
        if char in '({[': # catches the opening brackets
            stack.put(char) # puts opening bracket on the stack
        elif char in ')}]': # catches the closing brackets
            if stack.empty(): # if the stack is empty, there is no opening bracket for the closing one
                return False # so brackets are not ok
            right = stack.get() # gets the last opening bracket from the stack (first to be closed)
            if right != pairs[char]: # if the opening bracket does not match the closing one
                return False # brackets are not ok
    return stack.empty() # if the stack's empty all brackets have been closed properly
#True if brackets in expression are ok of False otherwise
# checking expression1
if brackets_ok(expression1):
    print("Expression 1 brackets are correct.")
else:
    print("Expression 1 brackets are NOT correct.")

# checking expression2
if brackets_ok(expression2):
    print("Expression 2 brackets are correct.")
else:
    print("Expression 2 brackets are NOT correct.")

# checking expression3
if brackets_ok(expression3):
    print("Expression 3 brackets are correct.")
else:
    print("Expression 3 brackets are NOT correct.")