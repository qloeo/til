# BOJ_7785_회사에있는사람.py
# n = int(input())
# N_list = [input() for _ in range(n) ]
N_list = ['Baha enter', 'Askar enter', 'Baha leave', 'Artem enter']
# print(N_list)
result = []
for i in N_list:
    # print(i)
    if i.endswith('enter'):
        result = i
N_list.sort()
print(result)
