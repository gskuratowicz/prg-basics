###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]
n = len(arr)

print(arr)
print('Number of elements', len(arr))
print('First value is ', arr[0])
print('Second valueis ', arr[1])
print('Last value is ', arr[n-1])
print('Last but one value is ', arr[n-2])
print('The sum of the first and last value is ', arr[0]+arr[1])
print('The middle value is ',arr[n//2])
for i in arr:
    print(i, end=" ")
    i +=1