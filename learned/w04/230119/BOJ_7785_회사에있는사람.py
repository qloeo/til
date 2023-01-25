# BOJ_7785_회사에있는사람.py

# inout_dic = {'Baha': 'leave', 'Askar': 'enter', 'Artem': 'enter'}

Test_Case = int(input())
log_dic ={}

for t in range(Test_Case):
    name, inout = map(str, input().split())
    log_dic[name] = inout
#     # print(log_dic)
#     # 키가 같을 경우 새로운 값으로 대체되기때문에 Baha는 leave로 바뀐다.

log_dic = sorted(log_dic, reverse = True)
# sorted() 정렬 함수 : 반환 값을 저장해야함
# sort() 저장이 되긴하나(반환값은 없음) 딕셔너리에서 사용 불가
# # 2기_5회차_장하늬
# ​for key in sorted(name_dict, reverse = True): 
#     if name_dict[key] == 'enter': print(key) #저 이렇게 했는데 백준에서 맞았다고 나왔어요..

for key, value in log_dic.items():
    # print(key, value)
    if value == 'enter':
        print(key)



# ### 인덱스로 키와 값 넣기
# # inout_dic = {'Baha': 'leave', 'Askar': 'enter', 'Artem': 'enter'}

# Test_Case = int(input())
# log_dic ={}

# for t in range(Test_Case):
#     name = input().split()
#     log_dic[name[0]] = name[1]
# #     # print(log_dic)
# #     # 키가 같을 경우 새로운 값으로 대체되기때문에 Baha는 leave로 바뀐다.

# for key, value in log_dic.items():
#     # print(key, value)
#     if value == 'enter':
#         print(key)
