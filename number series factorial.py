'''Write a program to find the sum of the following series  -  1 + x/1! + x2/2! + ……….xn/n!'''

n = int(input())
x = int(input())
f = 1
s = 1
y = 1
i = 1
while i<n:
    f = f*i
    v = (x)**y
    s = s+(v/f)
    y += 1
    i += 1
print(s)

