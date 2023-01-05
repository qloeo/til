"""
문제 6
양의 정수만 저장한 리스트가 주어집니다.
리스트에 저장된 정수 중 가장 큰 값을 출력하세요.
단, max() 함수는 사용하지 마세요.
"""

number_list = [1,2,3,4,5]

# max_value  = 0
max_value = 0 
# 만약, 수 제한이 없다면? 초기 값을 첫번째 값으로.
# max_value = number_list[0]
# number_list 반복, number!
for number in number_list:
    # 만약에 max_value보다 number가 크면!
    if max_value < number:
        # 값 교체
        max_value = number

print(max_value)