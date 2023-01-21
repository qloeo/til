# BOJ_10822_더하기.py

# S = "10,20,30,50,100"
S = str(input())
result = 0
S = S.split(',')
# print(S)

for s in S:
    result += int(s)
    # print(s)
    # print(type(s))
print(result)



