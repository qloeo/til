# 5. 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.
# 값이 100 초과 / 0 미만이면 '에러' 출력
# 값이 60 이상이면 '합격' 출력
# 값이 60 미만이면 '불합격' 출력

a = int(input('정수를 입력하세요 > '))

if a > 100 or a < 0 :
    print('에러')
elif a > 60 :
    print('합격')
else :
    print('불합격')