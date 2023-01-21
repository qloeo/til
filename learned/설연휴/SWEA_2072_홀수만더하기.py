# SWEA_2072_홀수만더하기.py
T = int(input())

for test_case in range(1, T+1):
    Numbers = list(map(int, input().split()))
    result = 0
    
    for n in Numbers:
        if n%2 == 1:
            result += n
    
    print(f'#{test_case} {result}')