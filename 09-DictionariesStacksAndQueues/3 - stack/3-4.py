import queue
stack = queue.LifoQueue()
def decimal_to_binary(n):
    while n > 0:
        remainder = n % 2
        stack.put(remainder)
        n = n // 2

    binary_number = ''
    while not stack.empty():
        binary_number += str(stack.get())
    return binary_number

print(decimal_to_binary(18))
