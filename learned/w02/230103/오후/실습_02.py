# 2. 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.
#   두 정수가 같으면 False를 출력하세요.

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))

if a > b :
    print(a)
elif a < b :
    print(b)
else :
    print('False')