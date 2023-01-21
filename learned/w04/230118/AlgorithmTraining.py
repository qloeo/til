# AlgorithmTraining.py

# 9498	시험 성적	https://www.acmicpc.net/problem/9498
Score = int(input())

if Score >=90 and Score<=100:
    print('A')
elif Score >=80 and Score<=89:
    print('B')
elif Score >=70 and Score<=79:
    print('C')
elif Score >=60 and Score<=69:
    print('D')
else:
    print('F')

# 9093	단어 뒤집기	https://www.acmicpc.net/problem/9093
TestCase = int(input())

for t in range(TestCase):
    String = list(map(str, input().split()))
    # String = ['I', 'am', 'happy', 'today']
    Result_list= []
    Result = ''

    for s in String[0:]:
        Result_list.append(s[::-1])
    # Result = ' '.join(map(str, Result_list))
    print(*Result)



# 11721	열 개씩 끊어 출력하기	https://www.acmicpc.net/problem/11721
String = input()

for s in range(0,len(String),10):
    print(String[s:s+10])



# 2947	나무 조각	https://www.acmicpc.net/problem/2947
Number_list = list(map(int,input().split()))
good_Numbers = [1,2,3,4,5]

while True:
    for i in range(len(Number_list)-1):
        if Number_list[i] > Number_list[i+1]:
            result = Number_list[i]
            Number_list[i] = Number_list[i+1]
            Number_list[i+1] = result
            print(*Number_list)
    if Number_list == good_Numbers :
        break

# 정호영쌤 풀이
input_numbers = "2 1 5 3 4" # 입력 문자열
numbers = input_numbers.split() # 숫자 리스트

for number in input_numbers:
    numbers.append(int(number))
while True:
    # 첫 번째 조각의 수 > 두 번째 조각의 수 ???
    if numbers[0] > numbers[1]:
        # 조건식이 성립하면 값을 교환
        numbers[0], numbers[1] = numbers[1], numbers[0]

        # 값을 확인1
        print(numbers)

    if numbers[1] > numbers[2]:
        numbers[1], numbers[2] = numbers[2], numbers[1]

        # 값을 확인2
        print(numbers)

    if numbers[2] > numbers[3]:
        numbers[2], numbers[3] = numbers[3], numbers[2]

    if numbers[3] > numbers[4]:
        numbers[2], numbers[4] = numbers[4], numbers[2]

        # 값을 확인3
        print(numbers)

    if numbers == [1, 2, 3, 4, 5]:
        break

    # 정호영쌤 풀이
input_numbers = "2 1 5 3 4" # 입력 문자열
numbers = input_numbers.split() # 숫자 리스트

for number in input_numbers:
    numbers.append(int(number))
while True:
    # 첫 번째 조각의 수 > 두 번째 조각의 수 ???
    if numbers[0] > numbers[1]:
        # 조건식이 성립하면 값을 교환
        numbers[0], numbers[1] = numbers[1], numbers[0]

        result = ""
        for number in numbers:
            result += str(number) + " "

        # 값을 확인1
        print(numbers)



    if numbers[1] > numbers[2]:
        numbers[1], numbers[2] = numbers[2], numbers[1]

        result = ""
        for number in numbers:
            result += str(number) + " "

        # 값을 확인2
        print(numbers)

    if numbers[2] > numbers[3]:
        numbers[2], numbers[3] = numbers[3], numbers[2]

    if numbers[3] > numbers[4]:
        numbers[2], numbers[4] = numbers[4], numbers[2]

        result = ""
        for number in numbers:
            result += str(number) + " "

        # 값을 확인3
        print(numbers)

    if numbers == [1, 2, 3, 4, 5]:
        break


## 반복문을 이용하여 줄이기
    for i in range(0, len(numbers) -1):
        print(i)
        if numbers[1] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        result = ""
        for number in numbers:
            result += str(number) + " "

        # 값을 확인
        print(numbers)
        if numbers == [1, 2, 3, 4, 5]:
            break

# 이중 반복문을 해결할때 처음부터 접근하면 어려우니 한단계씩 차근차근 풀어보시도록
# 작은 단위로 문제를 해결하기(중요!!)