# 1110.py
N = int(input())
# print(N//10)
# print(N%10)
s = N//10 + N%10
result = N%10 * 10 + s%10
i = 1

while N!= result:
    s = result//10 + result%10
    result = result%10 * 10 + s%10
    i+= 1
print(i)

