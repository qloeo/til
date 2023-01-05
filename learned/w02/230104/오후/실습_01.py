"""
문제 1
정수 한 개를 입력 받고, 해당 정수의 절대 값을 출력하세요.
단, abs() 함수는 사용하지 마세요.
"""

number = int(input('정수를 입력하세요 > '))

if number > 0:
    print(number)
else : 
    print(number * -1)