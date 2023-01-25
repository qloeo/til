# B0J_2941_크로아티아알파벳.py

Croatia = ["c=", "c-","dz=", "d-", "lj", "nj", "s=", "z="]

# S = input()
S = "ljes=njak"

for i in Croatia:
    if i in S: # 입력문자에 크로아티아 문자가 있으면
        S = S.replace(i,'*') # 그 문자를 '*'로 변환

# print(S)
print(len(S)) # 길이를 출력한다.