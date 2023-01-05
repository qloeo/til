# 실습_01.py
# 문자열을 입력 받고 문자열에서 e의 개수를 구해서 출력하세요.
# 단, count() 함수는 사용하지 마세요.

string = input("문자열을 입력하세요 > ")
count = 0

for number in string:
    count = count + 1

print(count)