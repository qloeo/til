# 06_BOJ_9012_괄호.py

T = int(input()) # Test_case

for Test_case in range(1,T+1):
    PS = str(input()) # 괄호들을 입력받아
    PS_list = list(PS[0:]) # 리스트로 만든다. 
    # print(PS_list) 

    while '('and ')' in PS_list: #만약 '(' 와 ')' 가 둘 다 있는 경우
        PS_list.remove('(')
        PS_list.remove(')') # 둘을 함께 지운다
    # print(PS_list)

    if len(PS_list) == 0: # 리스트 길이가 0이면 모두 짝을이뤄 지워졌으므로
        print('YES') # 'YES' 출력
    else: # 남아있을 경우 'NO' 출력
        print('NO')
# 장하늬님 의견
# 5회차_장하늬 — 오늘 오후 5:35
# line 10번을  while '(' in PS_list and ')' in PS_list:
# 연산자 우선순위 표 참고!!

# 5회차_장하늬 — 오늘 오후 5:25
T = int(input())

for t in range(T):
    PS = input()

    # PS의 개수가 1이 남기 전까지 돌려야 한다.
    while len(PS) > 1:
        if '()' in PS:
            strip_PS = PS.replace('()', "")
            PS = strip_PS
        else:
            break
           
    if PS == '':
        print('YES')
    else:
        print('NO')

# 5회차_왕나원 — 오늘 오후 5:42
T = int(input())

for i in range(T):
    stack = []
    string = input()

    for j in string:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: 
                print("NO")
                break
    else: 
        if not stack:
            print("YES")
        else: 
            print("NO")