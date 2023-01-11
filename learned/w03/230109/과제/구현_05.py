# 구현_05.py
# 단어 3개를 입력받고, 3개의 단어를 -로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지 마세요.
string_list = input('문자열을 입력하세요 > ').split()

# 방법 1
print(string_list[0], string_list[1], string_list[2], sep='-')

# 방법 2
print(*string_list, sep='-')