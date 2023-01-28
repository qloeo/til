# 230126_test.py

# 괄호 입력 테스트

# 0-1
# PS = list(map(str, input().split())) # 아... 띄어쓰기 입력이 아니구나..

# 0-2
# PS = str(input()) # 괄호입력
    # PS_list = [] # 리스트를 만든다.
    # for i in PS: # for문을 이용하여 , 입력된 괄호를  list로 변경
        # PS_list += i

# 1
# p = '()()(())'
# p_list = []
# for i in p:
#     p_list += i
# print(p_list)

# 2
PS = str(input())
PS_list = list(PS[0:])

print(PS_list)
