def f(d):
    count = 0
    for char in d:
        if char == "+":
            count += 1
        elif char == "-":
            count -= 1
    return count

if __name__ == "__main__":
    print(f(""))
    print(f("+-+"))
    print(f("+-+++-+---"))
    print(f("+-+++++-"))
