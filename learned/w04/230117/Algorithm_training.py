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

# 푸는중에 timeover ㅜㅜ