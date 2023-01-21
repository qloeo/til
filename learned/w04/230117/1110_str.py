N = input() # 입력값이자, 반복문을 끝낼 기준
given_n = N # N을 복사한 변수
cnt = 0 # 사이클 횟수

if int(given_n) < 10:
    given_n = "0" +given_n # 앞에 0을 붙여서 두 자리수로 만든다.

while True:
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