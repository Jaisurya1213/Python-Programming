s = "aabbccdedf"
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
odd_count = 0
mpal = ""
for i,count in freq.items():
    if count % 2 != 0:
        odd_count += 1
        mpal = i
        
if odd_count > 1:
    print("false")
else:
    hpal = ""
    
    for char in freq:
        hpal += char * (freq[char] // 2)
        palindrome = hpal + mpal + hpal[::-1]
    print(palindrome)
