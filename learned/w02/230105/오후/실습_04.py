"""
실습_04.py

이름, 전화번호, 거주지 정보를 입력받아 
딕셔너리 구조로 저장하고,
해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.

이름을 입력하세요 > 정우영
전화번호를 입력하세요 > 010-1234-5678
거주지를 입력하세요 > 서울시

"""

# dict_variable = {
#     "이름" : "" ,
#      "전화번호" : "",
#      "거주지" : "",
# }
# print(dict_variable)

# dict_variable["이름"] = input("이름을 입력하세요 > ")
# dict_variable["전화번호"] = input("전화번호를 입력하세요 > ")
# dict_variable["거주지"] = input("거주지를 입력하세요 > ")

# print(dict_variable)


name = input("이름을 입력하세요 > ")
phone_number = input("전화번호를 입력하세요 > ")
residence = input("거주지를 입력하세요 > ")
dict_variable = {
    "이름" : name,
    "전화번호" : phone_number,
    "거주지" : residence,
}
print(dict_variable)
for key, value in dict_variable.items():
    print(f"{key} : {value}")
