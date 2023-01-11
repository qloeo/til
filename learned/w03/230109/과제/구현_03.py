# 구현_03.py
# 문자열을 입력받고, e를 제거한 결과를 출력하세요.
# 단, replace() 메서드는 사용하지 마세요.

string = input('문자열을 입력하세요 > ')
new_string = ''
for char in string:
    if char != 'e':
        new_string += char
print(new_string)