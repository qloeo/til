# 02_BOJ_2729_세탁소사장동혁.py
T = int(input())

for Test_case in range(1,T+1):
    C = int(input())
    C_list = [0,0,0,0]
    
    while C >= 25:
        C_list[0] += 1
        C -= 25
    while C >= 10:
        C_list[1] += 1
        C -= 10
    while C >= 5:
        C_list[2] += 1
        C -= 5
    while C >= 1:
        C_list[3] += 1
        C -= 1
    print(*C_list)

# 4회차_김현민 — 오늘 오후 5:15
#세탁소 사장 동혁
T = int(input())
rest = [25,10,5,1]
for i in range(T):
    n = int(input())
    for j in range(4):
        print(n // rest[j],end=' ')
        n = n % rest[j]
    print()
