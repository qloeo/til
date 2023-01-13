# 조건 표현식
num = 2
value = '홀' if num %2 else '짝'
print(value)

# 반복문 enumerate순회

# 1~3의 세제곱의 결과가 담긴 리스트를 만드시오.
n_list = [1, 2, 3 ]
for number in range(1,4):
    n_list.append(number**3)
print(n_list)

[number**3 for number in range(1,4)]

# Dictionary Comprehension


# lambda [parameter] : 표현식
numbers = ['1', '2', '3']
# [1, 2, 3]으로 바꾸고 싶다면?
# int : 함수
new_numbers = list(map(int, numbers))
print(new_numbers)

numbers = [[2, 1], [1, 3]]
# 정렬
# sorted : 함수
print(list(map(sorted, numbers)))

numbers = [2, 4]
# 2로 나눈 몫으로만 그성된 [1, 2]

def div_2(n):
    return n//2
print(list(map(div_2, numbers)))
# lambda 이름, 정의 내리지않고 한번만 쓰는 식 : 익명함수
print(list(map(lambda n: n//2, numbers)))
# 조건표현식
print([ n//2 for n in numbers])
# 기본형식
new_number = []
for n in numbers:
    new_numbers.append(n//2)
print(new_numbers)