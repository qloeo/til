# 9085	더하기	https://www.acmicpc.net/problem/9085
Test_Case = int(input())

for t in range(Test_Case):
    N = int(input())
    Numbers = map(int, input().split())
    result = 0
    for n in Numbers:
        result += n
    print(result)

# 10824	네 수	https://www.acmicpc.net/problem/10824
Number_list = list(input().split())

AB = Number_list[0] + Number_list[1]
CD = Number_list[2] + Number_list[3]

AB, CD = int(AB), int(CD)

print(AB+CD)

# 권준혁(0)님 코드
A, B, C, D = list(map(str, input().split())) # input().split()만 써도 문자열로 받을듯_준혁님
print(int(A+B)+int(C+D))




# 3009	네 번째 점	https://www.acmicpc.net/problem/3009
point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))
point3 = list(map(int, input().split()))

X_min = min(point1[0],point2[0],point3[0])
Y_min = min(point1[1],point2[1],point3[1])
X_max = max(point1[0],point2[0],point3[0])
Y_max = max(point1[1],point2[1],point3[1])
# print(X_min,Y_min,X_max,Y_max)

rp1 = [X_min, Y_min]
rp2 = [X_max, Y_min]
rp3 = [X_min, Y_max]
rp4 = [X_max, Y_max]
# print(rp1,rp2,rp3,rp4)

# if rp1 != point1 and rp1 != point2 and rp1 != point3:
#     print(rp1)
# elif rp2 != point1 and rp2 != point2 and rp2 != point3:
#     print(rp2)
# elif rp3 != point1 and rp3 != point2 and rp3 != point3:
#     print(rp3)
# else :
#     print(rp4)

if rp1 != point1 and rp1 != point2 and rp1 != point3:
    print(int(rp1[0]),int(rp1[1]))
elif rp2 != point1 and rp2 != point2 and rp2 != point3:
    print(int(rp2[0]),int(rp2[1]))
elif rp3 != point1 and rp3 != point2 and rp3 != point3:
    print(int(rp3[0]),int(rp3[1]))
else :
    print(int(rp4[0]),int(rp4[1]))



# 10952	A+B - 5	https://www.acmicpc.net/problem/10952
while True:
    A, B = map(int,input().split())
    if A == 0 and B == 0:
        break
    else :
        print(A+B)

# 1110	더하기 사이클	https://www.acmicpc.net/problem/1110
N = int(input())
# print(N//10)
# print(N%10)
s = N//10 + N%10
result = N%10 * 10 + s%10
i = 1

while N!= result:
    s = result//10 + result%10
    result = result%10 * 10 + s%10
    i+= 1
print(i)



# 1110 더하기 사이클 string변환 풀이
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두자리 수를 만든다.
N = "26" # 입력값이자, 반복문을 끝낼 기준
given_n = N # N을 복사한 변수
cnt = 0 # 사이클 횟수

while True:
    if int(given_n) < 10:
        given_n = "0" +given_n # 앞에 0을 붙여서 두 자리수로 만든다.

    # 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합늬 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.

    # 각 자리의 숫자를 더한다.
    first = given_n[-1] # 1 자리수
    second = given_n[0] # 10의 자리수
    print(type(first),type(second))

    sum_number = int(first) + int(second)

    # 주어진 수 N
    # 구한 합 sum_number
    new_number = given_n[-1] + str(sum_number)[-1]
    print(new_number)

    # 연산 횟수 증가(사이클 횟수 증가)
    cnt += 1

    # 새로운 수가 기준과 값으면 반복문 종료
    if int(new_number) == int(N):
        break

    given_n = new_number
print(cnt)