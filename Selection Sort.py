def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        minval = i
        for j in range(i+1,n):
            if arr[j]<arr[minval]:
                minval = j
        minimum = arr.pop(minval) #arr[i],arr[minval]=arr[minval],arr[i]
        arr.insert(i,minimum)
    return arr
    
nums=[9,5,3,7,1,8,6,10,2]    
sol = selection_sort(nums)
print(sol)
