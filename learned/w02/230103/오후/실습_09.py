# 9. 정수 한 개를 입력 받고, 
# 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1 보다 작으면 False를 출력하세요.

n = int(input('정수를 입력하세요 > '))

if n < 1:
    print(False)
else:
    for element in range(1, n):
        if element % 2 ==1:
            print(element)