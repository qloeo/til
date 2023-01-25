# test.py



Test_Case = int(input())
log_dic ={}

import sys

for t in range(Test_Case):
    name, inout = map(str, sys.stdin.readline().split())
    log_dic[name] = inout
    print(log_dic)

print(log_dic)
# log_dic = sorted(log_dic, reverse = True)
# print(log_dic)

result = []
for key, value in log_dic.items():
    print(key, value)
    if value == 'enter':
        result.append(key)
result.sort(reverse = True) # 역순

for i in result:
    print(i)