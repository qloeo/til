
# 입출력 문제, 문제에서 주어지는 입력을 받기 적합한 입력 코드를 작성하세요.
# 입력과 똑같이 출력하는 코드를 작성하세요.
# 문제 1) 정수를 출력하세요
number = int(input('정수를 입력하세요 > '))
print(number)

# 문제 2) 단어를 구분해서 출력하세요. hello python world
string = input('단어들을 입력하세요 > ').split()
print(string)

# 문제 3) 테스트 케이스마다 입력 값을 그대로 출력하세요. 
# 테스트 케이스 수 3
T = int(input('테스트 수를 입력하세요 > '))
for t in range(1, T+1):
    print(t)
    pass

# 문제 4) 2개 이상의 정수를 출력하세요. 2 0 3 92 3
number_list = [1, 2, 3, 4, 5]
print(number_list)

# 문제 5) 2개의 정수를 출력하세요. 2 3
a, b = list(map(int, input().split()))
print(a, b)
# 문제 6) 단어를 구분해서 출력하세요. I am Programmer
string = input('단어들을 입력하세요 > ').split()
print(string)

# 문제 7) 테스트 케이스마다 입력 값을 그대로 출력하세요. 5
T = int(input('테스트 수를 입력하세요 > '))
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(t)

# 문제 8) 테스트 케이스 마다 입력값을 그대로 출력하세요. 5
T = int(input('테스트 수를 입력하세요 > '))
for t in range(1, T+1):
    #d여러개의 공백으로 구분된 정수 입력 받기
    numbers = list(map(int, input().split()))
    print(numbers)