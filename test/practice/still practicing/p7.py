
import re

def f(files):
    numbers = []

    # extract the number from each filename
    for name in files:
        match = re.search(r'\d+', name)
        numbers.append(int(match.group()))

    # pair filenames with their numbers
    paired = list(zip(numbers, files))

    # sort by the number
    paired.sort()

    # extract sorted filenames
    result = []
    for pair in paired:
        result.append(pair[1])

    return result

files = ["copy179","copy15","copy3","copy123","copy9"]  
print(f(files))
