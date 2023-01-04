# 7. 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
n1 = int(input('첫 번째 정수를 입력하세요 > '))
n2 = int(input('두 번째 정수를 입력하세요 > '))

if n1 < n2 :
    for elememt in range(n1 + 1, n2):
        print(element)

elif n1 > n2 :
    for element in range(n2 + 1, n1):
        print(element)

else :
    print(False)