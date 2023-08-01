# 1. What will be the output of the following python code
# A = [1, 2, 3,]
#     [4, 5, 6]
#     [7, 8, 9]
# [A[row][1]for row in (0, 1, 2)]

def is_Power_of_three(n):
    while (n % 3 == 0):
         n /= 3;         
    return n == 1;

print(is_Power_of_three(9))
print(is_Power_of_three(81))
print(is_Power_of_three(21))