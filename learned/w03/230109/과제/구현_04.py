# 구현_04.py
# 문자열과 알파벳을 공백으로 구분해서 입력받고, 문자열에서 입력한 알파벳 개수를 출력하세요.
# 단, count() 메서드는 사용하지 마세요.
string, alpha = input('문자열을 입력하세요 > ').split()
count = 0
for char in string:
    if char == alpha:
        count += 1

print(count)