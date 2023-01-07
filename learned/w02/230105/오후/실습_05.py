"""
실습_05.py
이름, 전화번호, 이메일, 거주지 정보를 입력받아
출력 예시와 동일한 딕셔너리 구조를 출력하세요.
Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다.
"""
# dict_variable = {
#     "정우영" : {
#         "전화번호" : "",
#         "이메일" : "",
#         "거주지" : "",
#     }
# }
# a = dict_variable["정우영"]

# print(dict_variable)

# a["전화번호"] = input("전화번호를 입력 해 주세요 > ")
# a["이메일"] = input("이메일을 입력 해 주세요 > ")
# a["거주지"] = input("거주지를 입력 해 주세요 > ")

# print(dict_variable)

name = input("이름을 입력하세요 > ")
phone_number = input("전화번호를 입력하세요 > ")
email = input("이메일을 입력하세요 > ")
residence = input("거주지를 입력하세요 > ")

dict_variable = {
    name: {
        "전화번호" : phone_number,
        "이메일" : email,
        "거주지" : residence,
    }
}
print(dict_variable)