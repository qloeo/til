# BOJ_2675_문자열반복.py

T = int(input())

for test_case in range(1,T+1):
    R , S = map(str, input().split())
    result = []
    R = int(R)
    for s in S:
        for r in range(1, R+1):
            result.append(s)
    print(*result, sep='')