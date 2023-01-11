# 구현_01.py
# 문자열을 입력받고, e가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e가 없으면 -1을 출력하세요.

# 풀이 1
string = input('문자열을 입력하세요 > ')
for index in range(len(string)):
    if string[index] == 'e':
        print(index)
        break
else:
    print(-1)

# 방법 2
string = input('문자열을 입력하세요 > ')
result = -1
for index in range(len(string)):
    if string[index] == 'e':
        result = index
print(result)