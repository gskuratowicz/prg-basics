def f(expression):
    stack = []
    items = expression.split()

    for item in items:
        if item.isdigit():
            stack.append(int(item))
        else:
            b = stack.pop()
            a = stack.pop()
            if item == '+':
                stack.append(a + b)
            elif item == '-':
                stack.append(a - b)

    return stack[0]

print(f("2 3 4 5 + - +"))
print(f("11 7 + 15 - 14 +"))
