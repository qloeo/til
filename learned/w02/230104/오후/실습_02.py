"""
문제 2
정수만 저장한 리스트가 주어집니다.
리스트 요소의 개수를 출력하세요.
단, len() 함수는 사용하지 마세요.
"""

number_list = [1, 2, 3, 4, 5]
count = 0

for number in number_list:
    count = count + 1

print(count)