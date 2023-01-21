# BOJ_2577_숫자의개수.py
# 23.01.19 못 푼 실습문제
import time
start = time.time()  # 시작 시간 저장

A , B , C = int(150), int(266), int(427)
# A, B, C = map(int, input().split())
ABC_mp = A * B * C
ABC_mp = str(ABC_mp)

# for i in range(0,10):
#     result = ABC_mp.count(str(i))
#     print(int(result))
# # 하 ... 이렇게 간단한거 였다니 ... 이걸 못풀고 있었다니 ..... ㅜㅜ
# 런타임 오류... 좋다말았네 .... ㅠㅠ

ABC_list = [0,0,0,0,0,0,0,0,0,0]
for n in ABC_mp:
    result = 0
    for i in range(0,10):
        if int(n) == i:
            ABC_list[int(n)] +=1
print(*ABC_list, sep = '\n')

# ... 런타임 오류

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간