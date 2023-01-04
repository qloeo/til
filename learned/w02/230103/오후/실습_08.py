# 8. 정수 두 개를 입력 받고, 
# 두 수 사이의 정수를 내림차순으로 
# 한 줄에 모두 출력하세요.
# 두 값이 같으면 False를 출력하세요.

n1 = int(input('첫 번째 정수를 입력하세요 > '))
n2 = int(input('두 번째 정수를 입력하세요 > '))

if n1 < n2:
    for element in range(n2 -1, n1, -1):
        print(element, end=" ")

elif n1 > n2:
    for element in range(n -1, n2, -1):
        print(element, end=" ")

else:
    print(False)