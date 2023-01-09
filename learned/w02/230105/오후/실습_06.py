"""
실습_06.py
문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.
단, count() 메서드는 사용하지 마세요.
"""
str = "hello"

# for str in enumerate(str):
#     print(str)


# str = "hello"
# str_list = [str[0],str[1],str[2],str[3],str[4]]

# print(str_list)

# for index, element in enumerate(str_list):
#     print(element, index)

# string = input("문자열을 입력하세요 > ")
string = [ 'apple', 'apple', 'tomato']
dict_variable = {}
for char in string:
    if char in dict_variable.keys():
        dict_variable[char] += 1
    elif char not in dict_variable.keys():
        dict_variable[char] = 1

for key, value in dict_variable.items():
    print(key, value)

print(dict_variable)