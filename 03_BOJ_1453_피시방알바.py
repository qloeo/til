# 03_BOJ_1453_피시방알바.py

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

# 5회차_권준혁(0) — 오늘 오후 5:19
# N = int(input())
# num = list(map(int,input().split()))
# cnt = 0
# lst = []
# for n in range (N) :
#     if num[n] in lst :
#         cnt += 1
#     else :
#         lst.append(num[n])
# print(cnt)
# 저는 좌석번호를 리스트에 추가해주고 리스트에 입력된 num과 같은 수가 있으면 cnt를 1씩 증가시켜서 cnt를 출력하는 방식으로 코드를 짜봤습니다