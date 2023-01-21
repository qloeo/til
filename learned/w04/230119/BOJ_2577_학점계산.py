# BOJ_2577_학점계산.py
Number_dic = {
    "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,
}

A = 150
B = 266
C = 427

ABC = A * B * C
ABC = str(ABC)
# print(ABC)
# print(type(ABC))
for n in ABC[0:]:
    # print(n)
    Number_dic[n] += 1
    print(Number_dic.get(n, 0))





# Number_dic[0] += 1
# print(Number_dic[0])
