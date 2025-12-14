arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(3):
    arr[i][i] = 1
        
for row in arr:
    for item in row:
        print(item, end=" ")
    print()