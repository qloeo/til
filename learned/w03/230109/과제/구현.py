# 구현.py

# 문제 1) 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1을 출력하세요.
# 단, index() / find() 메서드는 사용하지 마세요.

string = input('문자열을 입력하세요 > ')
i = 0

for result in string:
    i += 1
    result != "e"
    break

print(i)

# 문제 2) 문자열을 입력 받고, 각 단어의 등장 횟수를 출력 하세요.
# 단, count() 메서드는 사용하지마세요.

# str_list = list(input('단어들을 입력하세요 > ').split())
str_list = ['apple', ' apple', 'tomato', 'strewberry', 'tomato']
str_dict = {}

for char in string:
    if char in str_dict.key():
        str_dict[char] += 1
    elif char not in str_dict.key():
        str_dict[char] = 1

for key, value in str_dict.items():
    print(key, value)
print(str_dict)

# 문제 3) 문자열을 입력받고, e를 제거한 결과를 출력하세요.
# 단, replace() 메서드는 사용하지 마세요.

str = input('문자열을 입력하세요 > ')
str.strip("e")


# 문제 4) 문자열과 알파벳을 공백으로 구분해서 입력받고, 문자열에서 입력한 알파벳의 개수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.
a, b = input('문자열을 입력하세요 > ').split()
count = 0

for i in a:
    i == b
    count += 1

print(count)

# 문제 5) 양의 정수 3개를 입력받고, 3개의 양수를 -로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지 마세요.
a, b, c = map(int, input('숫자를 입력하세요 > ').split())
print(f'{a}-{b}-{c}')

