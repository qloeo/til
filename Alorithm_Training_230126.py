# Alorithm_Training_230126.py

# 10101	삼각형 외우기	https://www.acmicpc.net/problem/10101
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
# 틀렸습니다!!!!!
# input을 좀 더 간결하게 손보고, 나머지도 전체적으로 다시 해봐야겠다 ㅠㅠ


# 2720	세탁소 사장 동혁	https://www.acmicpc.net/problem/2720
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
# 맞았습니다!!!


# 1453	피시방 알바	https://www.acmicpc.net/problem/1453
N = int(input())
N_list = list(map(str, input().split()))
result = 0

for i in range(1, N+1):
    for n in N_list:
        count = 0
        count = N_list.count(n)
        print(count)
        if count >= 1:
            result += count
            result -= 1
    print(result)
# 아 .... 카운트를 각 인덱스 마다 했더니 값이 중복됬다.... 
# 다시 처음부터 해야할듯 ㅠㅠ 흑....


# 10773	제로	https://www.acmicpc.net/problem/10773
T = int(input())
K_list = []

for Test_case in range(1, T+1):
    K = int(input())
    if K != 0:
        K_list.append(K)
    elif K == 0:
        K_list.pop()
print(sum(K))
# 런타임 에러!!


# 2161	카드1	https://www.acmicpc.net/problem/2161


# 9012	괄호	https://www.acmicpc.net/problem/9012
T = int(input()) # Test_case

for Test_case in range(1,T+1):
    PS = str(input()) # 괄호들을 입력받아
    PS_list = list(PS[0:]) # 리스트로 만든다. 
    # print(PS_list) 

    while '('and ')' in PS_list: #만약 '(' 와 ')' 가 둘 다 있는 경우
        PS_list.remove('(')
        PS_list.remove(')') # 둘을 함께 지운다
    # print(PS_list)

    if len(PS_list) == 0: # 리스트 길이가 0이면 모두 짝을이뤄 지워졌으므로
        print('YES') # 'YES' 출력
    else: # 남아있을 경우 'NO' 출력
        print('NO')
    # 런타임 에러(ValueError)!! ㅠㅠ
    # 코딩 리뷰를 통해 원인을 찾았습니다!! ㅎㅎㅎ 
    # 오늘 다시 해봐야겠네요