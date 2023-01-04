# 11. 조건문, 리스트, 반복문
list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    if element < 0:
        continue
    print(element, end=" ")
# 3 5 1 9 21 % 