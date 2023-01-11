# 구현_02.py
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.
# 단, count() 메서드는 사용하지 마세요.

string = input('문자열을 입력하세요 > ').split()
dict_var = {}

for word in string:
    if word in dict_var:
        dict_var[word] += 1

    elif word not in dict_var:
        dict_var[word] = 1

for key, value in dict_var.items():
    print(f'{key} {value}')
