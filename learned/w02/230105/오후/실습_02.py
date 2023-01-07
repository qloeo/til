# 실습_02.py
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.
# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)

string = input("문자열을 입력하세요 > ")
count = 0

for char in string:
    if(
        char == "e"
        or char == "E"
        or char == "a"
        or char == "A"
        or char == "i"
        or char == "I"
        or char == "o"
        or char == "O"
        or char == "u"
        or char == "U"
    ):
        count += 1

print(count)

