# 입출력예시코드.py
# 정수 1개 입력 받기
number = int(input())
print(number)

# 공백으로 구분된 여러개의 정수 입력 받기
numbers = list(map(int, input().split()))
print(numbers)

# 공백으로 구분된 여러개의 단어 입력 받기
string = input().split()
print(string)

# 공백으로 구분된 2개의 정수 입력 받기
a, b = list(map(int, input().split()))
print(a, b)

# 테스트 케이스 수가 주어지는 입력 받기
T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    print(t)
    # 이하 입력 코드
    pass

# 입력 줄 수가 주어지는 입력 받기
N = int(input()) # 입력 줄 수

for _ in range(N):
    # 이하 입력 코드
    pass

# 테스트 케이스와 입력 줄 수가 주어지는 입력 받기
T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input()) # 입력 줄 수

    for _ in range(N):
        # 이하 입력 코드
        pass

# 파일 입력
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
import sys
sys.stdin = open('input.txt', 'r')
# 이하 입력코드