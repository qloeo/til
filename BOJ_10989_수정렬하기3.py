# BOJ_10989_수정렬하기3.py
# import sys

N = int(input())

# Numbers = [sys.stdin.readline().strip() for i in range(N)]
# sys는 메모리초과... ㅜㅜ
Number_list = []

for n in range(N):
    Number = int(input())
    Number_list.append(Number)

Number_list.sort()

print(*Number_list, sep = "\n")