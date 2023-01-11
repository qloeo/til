
# 문제 6) 양의 정수를 입력받고, 자리수의 합을 출력하세요.
# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지 마세요. str() 함수를 사용하지 마세요.

# 내 오답
# numbers = int(input('양의 정수를 입력하세요 > '))

# for number in numbers:
#     number += numbers
#     if numbers > 0 :
#         print('-1')
# print(number)
# 내 오답 끝

# str() 사용 할 경우
n = input()
result = 0
for i in n:
    result += int(i)

print(result)

# while 사용
# 반복적으로 n을 10으로 나눈 몫,
# n이 0 보다 클 때 계속 반복!
# 결과 값은 n을 10으로 나눈 나머지를 더해나갈 것이다.

n= int(input())

if n < 0:
    print(-1)
else:
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
        #print(n, result)
        print(result)

number = int(input('양의 정수를 입력하세요 > '))
if number <0:
    print(-1)
else:
    total = 0
    while number > 0:
        n = number % 10
        total = total + n
        number = number // 10
    print(total)

