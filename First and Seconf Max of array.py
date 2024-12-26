arr=[111,17,5,18,3]
if arr[0] > arr[1]:
    fmax = arr[0]
    smax = arr[1]
else:
    fmax = arr[1]
    smax = arr[0]
for i in arr[2:]:
    if i>fmax:
        smax=fmax
        fmax=i
    elif(smax<i):
        smax=i
print(fmax)
print(smax)
