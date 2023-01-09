# 입출력연습.py
# 입출력 예시코드

# 정수 1개 입력 받기
number = int(input())
print(number)

# 공백으로 구분된 여러개의 정수 입력 받기
numbers = list(map(int,input().split()))
print(numbers)

# 공백으로 구분된 여러개의 단어 입력 받기
string = input().split()
print(string)

# 공백으로 구분된 2개의 정수 입력 받기
a, b = list(map(int, input().split()))
print(a,b)

# 리스트
numbers = list(map(int, input().split()))
#asterisk, * , 언패킹
print(*numbers)

# for 문
numbers = list(map(int, input().split()))
for number in numbers:
    print(number, end=" ")



# 문제 1) 5를 입력받아보세요.

number = int(input())
print(number)

# 문제 2) 2 5 를 입력 받아서 출력하세요.
n1, n2 = map(int, input().split())
print(n1, n2)

# 문제 3) 1 2 3 을 입력받아서 출력하세요.
n3, n4, n5 = map(int, input().split())
print(n3, n4, n4)

# 문제 4) word1 word2 word3
string = input().split()
print(string)

# 문제 5) 1 2 3 4 5
numbers = list(map(int, input().split()))
print(numbers)

# 문제 6) -10 10
a, b = list(map(int, input().split()))
print(a, b)

# 문제 7) a b c d e
string = input().split()
print(string)

# 문제 8) 3 17 1 39 8 41 2 32 99 2
numbers = list(map(int, input().split()))
print(numbers)

# 문제 9) 1 4 0 10 2 3 9
numbers = list(map(int, input().split()))
print(numbers)