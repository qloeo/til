# 10. 조건문, range, 반복문
n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if n < 0:
        break

# 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9

print("=====")

n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if element < 0:
        break

# 10 9 8 7 6 5 4 3 2 1 0 -1