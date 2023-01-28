# BOJ _10773_제로.py

T = int(input())
K_list = []

for Test_case in range(1, T+1):
    K = int(input())
    if K != 0:
        K_list.append(K)
    elif K == 0:
        K_list.pop()

# 탁희쌤 풀이
    # if K == 0:
    #     K_list.pop()
    # else:
    #     K_list.append(K)

print(sum(K))