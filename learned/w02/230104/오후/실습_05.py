"""
문제 5
정수만 저장한 리스트가 주어집니다.
리스트에 저장된 정수들의 곱을 출력하세요.
"""
number_list = [-1, -2, 3]
prod = 1
for number in number_list:
    prod = prod * number
print(prod)
