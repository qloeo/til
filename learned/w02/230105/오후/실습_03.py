# 실습_03.py
# 입력과 같은 딕셔너리 변수가 있을 때,
# 해당 인물의 나이를 출력하세요.
dict_variable = {
    "이름" : "정우영",
    "생년" : "2000",
    "회사" : "하이퍼그로스",
}

dict_variable["나이"] = 2023 - int(dict_variable["생년"]) + 1

print(dict_variable["나이"])