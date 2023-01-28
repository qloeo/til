# 01_BOJ_10101_삼각형외우기.py
A = int(input())
B = int(input())
C = int(input())
# A = 60
# B = 70
# C = 50


ABC_sum = A + B + C

if A == B == C:
    print('Equilateral')
elif ABC_sum == 180 and A == B or A == C or B ==C:
    print('lsoscalene')
elif ABC_sum == 180 and A != B and A != C and B != C:
    print('Scalene') 
else:
    print('Error')