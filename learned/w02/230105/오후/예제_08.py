# 예제_08.py
# 리스트 , 예외 처리

list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])

except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
list_variable[3]은 없는데 값을 출력하라고 하였습니다.
"""