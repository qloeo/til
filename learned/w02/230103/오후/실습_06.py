# 6. 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
# - 흰트 : 문자열 역 슬라이싱
a = input('문자열을 입력하세요 > ')

for element in a[::-1]:
    print(element)
    