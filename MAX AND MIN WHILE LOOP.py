''' WHILE LOOP MAX AND MIN'''


n = int(input())
i = 0
arr =[]
a = int(input())
arr.append(a)
ma = a
mi = a
while i<n:
    a = int(input())
    arr.append(a)
    if arr[i]>ma:
        ma = arr[i]
    if arr[i]<mi:
        mi = arr[i]
    i = i+1
print(ma)
print(mi)
