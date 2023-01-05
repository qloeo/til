"""
문제 7
양의 정수만 저장한 리스트가 주어집니다. 
리스트에 저장된 정수 중 가장 작은 값을 출력하세요.
단, min() 함수는 사용하지 마세요.
"""

number_list = [1, 2, 3, 4, 5]

min_value = number_list[0] # 0 기준이면 0이거나 0보다 적은수가 있기때문

for number in number_list:
    if number < min_value:
        min_value = number
print(min_value)
