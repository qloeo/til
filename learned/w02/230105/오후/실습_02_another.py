# 실습_02_another
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.
# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)

string = input("문자열을 입력하세요 > ")
count = 0

for char in string:
    if char in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        count += 1
        
print(count)
