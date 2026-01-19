def f(files):
    split_files = []
    for string in files:
        name, extension = string.split(".")
        split_files.append((extension, string))
    
    split_files.sort()

    result = []
    for extension, filename in split_files:
        result.append(filename)
    
    return result
    
        

files = ["a.txt","bb.pdf","ccc.py","dddd.mpeg4"]  
print(f(files))  
