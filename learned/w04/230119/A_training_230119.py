# 2576	홀수	https://www.acmicpc.net/problem/2576

Number = 0
result = 0 # 홀수 합
Com_Number = 100 # 홀수 최솟값
i = 0

while True:
    Number = int(input())
    i += 1
    if Number%2 == 1: # Number가 홀수면
        result += Number
        # print(Number)
        # print(result)
        if Com_Number > Number:
            Com_Number = Number
        
    if i == 7:
        break

if result == 0:
    print(-1)     
else:
    print(result)
    print(Com_Number)

# 10822	더하기	https://www.acmicpc.net/problem/10822

# S = "10,20,30,50,100"
S = str(input())
result = 0
S = S.split(',')
# print(S)

for s in S:
    result += int(s)
    # print(s)
    # print(type(s))
print(result)


# 2754	학점계산	https://www.acmicpc.net/problem/2754

Grade_dic = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0,
}

Grade = input()

print(Grade_dic[Grade])



# 5622	다이얼	https://www.acmicpc.net/problem/5622


dial_dic = {
    "A":2, "B":2, "C":2,
    "D":3, "E":3, "F":3,
    "G":4, "H":4, "I":4,
    "J":5, "K":5, "L":5,
    "M":6, "N":6, "O":6,
    "P":7, "Q":7, "R":7, "S":7,
    "T":8, "U":8, "V":8,
    "W":9, "X":9, "Y":9, "Z":9,
}

Alphabet = input()
result = 0

for a in Alphabet:
    # print(a)
    # print(dial_dic[a])
    result += dial_dic[a]
    result += 1
print(result)

# 4회차_김현민 님 list 풀이
s = input()
time = 0
answer = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in s:
    for j in range(len(answer)):
        if i in answer[j]: 
            time = time + j+3
print(time)





# 2577	숫자의 개수	https://www.acmicpc.net/problem/2577





# 7785	회사에 있는 사람	https://www.acmicpc.net/problem/7785


# inout_dic = {'Baha': 'leave', 'Askar': 'enter', 'Artem': 'enter'}

Test_Case = int(input())
log_dic ={}

for t in range(Test_Case):
    name, inout = map(str, input().split())
    log_dic[name] = inout
#     # print(log_dic)
#     # 키가 같을 경우 새로운 값으로 대체되기때문에 Baha는 leave로 바뀐다.

for key, value in log_dic.items():
    # print(key, value)
    if value == 'enter':
        print(key)
