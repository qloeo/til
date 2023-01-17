# 10039	평균 점수	https://www.acmicpc.net/problem/10039
s_sum = 0
for s in range(5):
    student = int(input())
    if student >= 40:
        s_sum += student
    else :
        s_sum += 40
print(int(s_sum/5))

# 10871	X보다 작은 수	https://www.acmicpc.net/problem/10871
Test_case, X = map(int, input().split())
A_list = list(map(int, input().split()))

for t in A_list:
    if t < X:
        print(t, end=' ')
# 하 ... TestCase에 속아서 삽질. 솔직히 필요도 없는데, 변수에 포함시키다니.. 너무해ㅠㅠ


# 2480	주사위 세개	https://www.acmicpc.net/problem/2480
A, B, C = list(map(int,input().split()))
if A==B and A==C:
    print(10000+A*1000)
elif A==B or A==C:
    print(1000+A*100)
elif B==C:
    print(1000+B*100)
elif A > B and A > C:
    print(A*100)
elif B > A and B > C:
    print(B*100)
else :
    print(C*100)
# f쓰다보니 변수에 무조건 중괄호를 붙임... 바보...


# 10886	0 = not cute / 1 = cute	https://www.acmicpc.net/problem/10886
Test_Case= int(input())
cute = 0
not_cute = 0

for t in range(Test_Case):
    n = int(input())
    if n == 1:
        cute += 1
    elif n == 0:
        not_cute += 1
if cute > not_cute:
    print('Junhee is cute!')
else :
    print('Junhee is not cute!')
# Test_Case 입력값 3을 기준으로 잘못 적용 > 비교연산자를 사용해 몇개의 데이터가 들어오더라도 올바른 결과값이 출력됨

# 2506	점수계산(콤보)	https://www.acmicpc.net/problem/2506
Count = int(input())
Score = map(int, input().split())
Point = 0
Result = 0

for i in Score:
    if i == 1:
        Point += 1
        Result += Point
    else :
        Point = 0
print(Result)
# if문 중첩이 필요한듯 보였으나, 노트에 적다보니 의외로 간단하게 나옴. 많은 숫자에 기가죽어 풀이를 미뤘는데...기분이 좋군 ㅋ

#0117비모쌤 풀이
# N = "10"
# answers = "1 0 1 1 1 0 0 1 1 0"
N = input()
answers = input()

N = int(N)
# print(type(N), N)
# map없이 해보자
answers = answers.split()
# print(answers)
numbers = []
for answer in answers:
    numbers.appdnd(int(answer))
# print(N)
# print(numbers)

total = 0 # 총합을 저장할 변수
score = # 연속으로 맞춘 개수를 저장할 변수
for number in numbers:
    # 1이면 정답, 0이면 오답
    if number ==1:
        # 정답일 때 연속으로 맞춘 개수 up
        score = score + 1
        total = total +score
    if number == 0:
        # 오답일 때 연속으로 맞춘 개수 0 초기화
        score = 0
        total = total + 0
        pass
    # print(number, score)
print(total)

# while 반복문으로도 풀어보자!