# BOJ_2161_카드1.py
# N = int(input())
N = int(7)
# # 숫자 리스트 만들기
# N_list = []
# for n in range(1, N+1):
#     N_list.append(n)
    # print(N_list)

# 탁희쌤 풀이
# N_list = [i for i range(1, N+1)]
N_list = list(range(1, N+1))
result_list = []

# 1장 남을때까지 반복 => while
while len(N_list) > 1:
    # 우선, 제일 위에 있는 카드를 바닥에 버린다.
    # N_list에서 제일 위 : pop(0)
    result_list.append(N_list.pop(0))
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김다.
    N_list.append(N_list.pop(0))
    print(result_list, N_list)

# '*'는 unpacking
print(*result_list, N_list[0])