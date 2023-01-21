# 11720.py
N = int(input())
Numbers = input()
Number_list = list(Numbers)
result = 0

for n in Number_list:
    result += int(n)
print(result)