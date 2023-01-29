# BOJ_2562_최댓값.py
import sys

Numbers = [sys.stdin.readline().strip() for i in range(9)]

# Numbers = ['3', '29', '38', '12', '57', '74', '40', '85']
Numbers = list(map(int, Numbers))

max_Number = max(Numbers)
print(max_Number)
print(Numbers.index(max_Number)+1)