# 창원시장배_파크골프대진표.py

import sys
sys.stdin = open("input_parkgolf.txt", "r")

n = int(input())

# 리스트 맵함수로 입력받기.
name_list = [list(map(str, input().split())) for _ in range(n)]
print(name_list)

# 이중리스트는 행먼저. 행(세로) -> 열(가로)

print(name_list[0][0])
print(name_list[1][0])
print(name_list[2][0])

