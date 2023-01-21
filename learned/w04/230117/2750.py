# 2750.py
N = int(input())
Number_list = []

for t in range(N):
    Number = int(input())
    Number_list.append(Number)
    # print(Number_list)
Number_list.sort()
for i in range(N):
    print(Number_list[i])