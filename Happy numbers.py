def sum_of_squares(num):
    num_str = str(num)
    if num == 1:
        return 1
    res = 0
    for digit in num_str:
        res += int(digit) ** 2 
        if res!=1 and res!=7:
            return 1
    return sum_of_squares(res)
num = 76
result = sum_of_squares(num)
print(result)
