a =- 10
if  a >= 0:
    print('양수')
else :
    print('음수')

n = int(input())
if n%2 == 1:
    print('홀수')
else :
    print('짝수')

if n%2 :
    print('홀수')
else :
    print('짝수')

dust = int(input())
if dust <=30:
    print('좋음')
elif dust <=80:
    print('보통')
elif dust <=150:
    print('나쁨')
else :
    print('매우나쁨')

dust = 80
if dust >150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust >30:
    print('보통')
else:
    print('좋음')
print('미세먼지 확인완료')

dust = 500
if dust >150:
    print('매우나쁨')
    if dust >300:
        print('실외 활동을 자제하세요.')
    elif dust >80:
        print('나쁨')
    elif dust > 30:
        print('보통')
    else:
        if dust >= 0;
            print('좋음')
        else:
            print('값이 잘못되었습니다.')