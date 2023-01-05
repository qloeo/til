"""
문제 4
정수만 저장한 리스트가 주어집니다.
리스트에 저장된 정수들의 평균을 출력하세요.
단, len()/sum() 함수는 사용하지 마세요.
"""

number_list = [2, 4, 6]

total = 0
count = 0
for number in number_list:
    total = total + number
    count = count + 1

print(total / count)